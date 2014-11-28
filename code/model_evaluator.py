#!/usr/bin/env python

from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import roc_auc_score
import numpy as np

model = joblib.load('LogReg.pkl')
print 'loading val X'
v_X = joblib.load('v_X.pkl')
print 'loading val Y'
v_Y = joblib.load('v_Y.pkl')

predicted = model.predict(v_X)
probs = model.predict_proba(v_X)
print np.amin(probs[:, 0])
print np.amax(probs[:, 0])
print predicted.shape
print v_Y.shape
auc = roc_auc_score(v_Y, predicted)
print 'auc is: ' + str(auc)
print sum(predicted) / 1443984.0
print sum(v_Y) / 1443984.0
print model.score(v_X, v_Y)
