#!/usr/bin/env python

'''
Splits the feature matrix into training/validation data.
Also normalizes the features. It is expected that the user
run shuf to shuffle the input feature matrix before splitting them.

Input: INPUT - input feature matrix

Output: X - pickled training features
		Y - pickled training labels
		v_X - validation features
		v_Y - validation labels

Author: Alan Kao
'''

import numpy as np
import joblib

INPUT = 'agg_output.txt'

print 'loading input data'
data = np.loadtxt(INPUT, delimiter = '\t')

numCol = data.shape[1]
numRow = data.shape[0]
print 'num col: ' + str(numCol)

print data.shape
for c_i in range(1,numCol):
	col = data[:, c_i]
	col = col - np.mean(col)
	s = np.std(col)
	if s != 0:
		col = col / s
	data[:, c_i] = col

print 'finished regularizing'

numTraining = int(numRow * 0.8)
print 'num X instances: ' + str(numTraining)

print 'splitting X'
X = data[:numTraining, 1:]
print 'splitting Y'
Y = data[:numTraining, 0]

print 'splitting val X'
v_X = data[numTraining:, 1:]
print 'splitting val Y'
v_Y = data[numTraining:, 0]

print 'X shape: ' + str(X.shape)
print 'Y shape: ' + str(Y.shape)

print 'val X shape: ' + str(v_X.shape)
print 'val Y shape: ' + str(v_Y.shape)

print 'dumping X'
joblib.dump(X, 'X.pkl')
print 'dumping Y'
joblib.dump(Y, 'Y.pkl')
print 'dumping val X'
joblib.dump(v_X, 'v_X.pkl')
print 'dumping val Y'
joblib.dump(v_Y, 'v_Y.pkl')
