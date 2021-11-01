import cv2
from svgpathtools import svg2paths2
import numpy as np
import re
import pandas
import os

def get_word_list():
    pattern = "[M|L] (?P<X>\d+.\d+) (?P<y>\d+.\d+)"
    transcriptions = pandas.read_csv('ground-truth/transcription.txt', delimiter=' ', header=None,
                                     names=["id", "transcription"], index_col=0)
    word_list = list()
    images = [os.path.splitext(filename)[0] for filename in os.listdir('images/')]
    ##### per word / image
    for image_name in images:
        img = cv2.imread(f"images/{image_name}.jpg", cv2.IMREAD_GRAYSCALE)
        _, attributes, _ = svg2paths2(f"ground-truth/locations/{image_name}.svg")

        for word in attributes:
            # create empty mask
            mask = np.zeros(img.shape[0:2], dtype=np.uint8)

            matches = re.findall(pattern, word['d'])
            points = np.array([[int(float(x)), int(float(y))] for x, y in matches])

            cv2.drawContours(mask, [points], -1, (255, 255, 255), -1, cv2.LINE_AA)
            res = cv2.bitwise_and(img, img, mask=mask)
            rect = cv2.boundingRect(points)  # returns (x,y,w,h) of the rect

            ## crate the white background of the same size of original image
            wbg = np.ones_like(img, np.uint8) * 255
            cv2.bitwise_not(wbg, wbg, mask=mask)

            # overlap the resulted cropped image on the white background
            dst = wbg + res
            cropped = dst[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]

            # Do OTSU Thresholding
            _, thresholded = cv2.threshold(cropped, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            shape = thresholded.shape
            max_size = max(shape)
            x_padding = int((max_size - shape[0]) / 2)
            y_padding = int((max_size - shape[1]) / 2)
            squared = cv2.copyMakeBorder(thresholded, x_padding, x_padding, y_padding, y_padding, cv2.BORDER_CONSTANT,
                                         value=(255, 255, 255))

            resized = cv2.resize(squared, (100, 100))  # resized to 100x100 px

            word_list.append({
                'id': word['id'],
                'word_img': resized,
                'transcription': transcriptions.loc[word['id']]['transcription']

            })
    return word_list
