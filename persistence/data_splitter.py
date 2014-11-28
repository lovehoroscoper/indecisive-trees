#!/usr/bin/env python

import numpy as np
import joblib

INPUT = 'agg_out.txt'

data = np.loadtxt(INPUT, delimiter = '\t')

numCol = data.shape[0]
numTraining = int(numCol * 0.8)

X = data[:numTraining, 1:]
Y = data[:numTraining, 0]

v_X = data[numTraining:, 1:]
v_Y = data[numTraining:, 0]

print X.shape
print Y.shape

print v_X.shape
print v_Y.shape

joblib.dump(X, 'X.pkl')
joblib.dump(Y, 'Y.pkl')
joblib.dump(v_X, 'v_X.pkl')
joblib.dump(v_Y, 'v_Y.pkl')