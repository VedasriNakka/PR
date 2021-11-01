import numpy as np


def features(image):
    """
    compute features for an image
    :param image: word image of size 100x100 px
    :return: x: vector containing 100 features vectors (for each sliding windows)
    """
    x = []
    last_len_lc_uc = 0
    for j in range(100):
        window = image[:, j]    # sliding window of 1x100 px
        feature_vector = []
        bw_transition, black_px, lower_contour, upper_contour = 0, 0, 0, 0
        last_px_seen, lc_seen = window[0], False
        for i in range(100):
            if (last_px_seen == 255 and window[i] != 255) or (last_px_seen != 255 and window[i] == 255):
                bw_transition += 1
            if window[i] != 255:
                black_px += 1
                if not lc_seen:
                    lower_contour = i
                    lc_seen = True
                upper_contour = i
            last_px_seen = window[i]

        if upper_contour == lower_contour and black_px != 0:
            len_lc_uc = 1
            gradient = np.abs(len_lc_uc - last_len_lc_uc)
            black_px_over_lu_uc = 1
        elif upper_contour == lower_contour and black_px == 0:
            len_lc_uc = 0
            gradient = np.abs(len_lc_uc-last_len_lc_uc)
            black_px_over_lu_uc = 0
        else:
            len_lc_uc = np.abs(lower_contour - upper_contour) + 1
            gradient = np.abs(len_lc_uc-last_len_lc_uc)
            black_px_over_lu_uc = black_px/len_lc_uc

        last_len_lc_uc = len_lc_uc                      # update LC_{i-1},UC_{i-1}

        feature_vector.append(bw_transition)            # number of b/w transition
        feature_vector.append(black_px)                 # number of black pixels
        feature_vector.append(lower_contour)            # index of lower contour
        feature_vector.append(upper_contour)            # index of upper contour
        feature_vector.append(black_px_over_lu_uc)      # fraction of black pixels between LC and UC
        feature_vector.append(gradient)                 # gradient : difference of LC_i,UC_i to LC_{i-1},UC_{i-1}

        x.append(feature_vector)

    return x
