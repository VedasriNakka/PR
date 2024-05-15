#!/usr/bin/env python3
# Pattern Recogniton 2019 - Sample Solution Exercise 1a - KNN
# by Paul Maergner
#------------------------------------
import sys
from datetime import datetime
import csv
import numpy as np
import scipy.spatial

def read_data(filename):
	with open(filename, 'r') as f:
		reader = csv.reader(f)
		data = list(reader)
	matrix = np.array(data, dtype = int)
	# separate labels from samples
	samples = matrix[:,1:]
	labels = matrix[:,0]
	return labels, samples


def print_indent(text, indent, indent_char='\t'):
	print('{indent}{text}'.format(indent=indent*indent_char, text=text))
	sys.stdout.flush()


def my_euclidean(x, y):
	z = x-y
	ans = sum(z*z)**0.5
	return ans


def my_euclidean2(x, y):
	z = x-y
	ans = (z*z).sum()**0.5
	return ans


def my_euclidean3(x, y):
	z = x-y
	return np.linalg.norm(z)


def my_euclidean4(x, y):
	z = x-y
	ans = np.dot(z,z)
	return ans


def my_cosine(x, y):
	a = np.linalg.norm(x)
	b = np.linalg.norm(y)
	ans = 1.0 - (np.dot(x, y) / (a*b))
	return ans


def my_cityblock(x,y):
	return np.abs(x - y).sum()


def main():
	# input files
	train_filename = 'train.csv'
	test_filename = 'test.csv'

	# List of values for k
	k_list = [1, 3, 5, 10, 15]

	# List of metrics
	metrics = ['cosine', my_cosine, 'euclidean', my_euclidean4, my_euclidean3, my_euclidean2, my_euclidean, 'cityblock', my_cityblock]

	train_labels, train_samples = read_data(train_filename)
	test_labels, test_samples = read_data(test_filename)

	for m in metrics:	
		print_indent('metric: {metric}'.format(metric=m), indent=0)

		# compute all the distances (rows (outer list): test, columns (inner list): train)
		start_total = datetime.now()
		dist = scipy.spatial.distance.cdist(test_samples, train_samples, m)
		end = datetime.now()
		print_indent('metric runtime: {duration}'.format(duration=end-start_total), indent=0)

		for k in k_list:
			print_indent('k = {k}'.format(k=k), indent=1)
			
			# start timing
			start = datetime.now()

			# get k indices (per test sample) with the k smallest distances. each index corresponds to one test sample
			idx = np.argpartition(dist,k)
			idx = idx[:,0:k]
			
			# apply those indices to the training labels to get the k nearest neighbours for each test sample
			neigh = [train_labels[row] for row in idx]
			
			# find the neighbour that occurs the most for each test sample
			if k == 1 :
				predictions = np.concatenate(neigh)
			else :
				predictions = [np.argmax(np.bincount(row)) for row in neigh]
				
			# end timing
			end = datetime.now()

			# calculate the accuracy
			acc = np.count_nonzero(test_labels==predictions)/len(test_labels)

			print_indent('accuracy: {percent:.4f}%'.format(percent=acc*100), indent=2)
			print_indent('runtime: {duration}'.format(duration=end-start), indent=2)

		end = datetime.now()
		print_indent('Total runtime: {duration}'.format(duration=end-start_total), indent=1)


if __name__ == '__main__':
	main()
