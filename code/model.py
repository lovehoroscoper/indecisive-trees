#!/usr/bin/env python

'''
Author: Alan Kao

Creates Logistic Regression model and validates its performances using
AUC. Given a set of hyperparameters (C), prints the AUC corresponding to
each. Requires pre-pickled datasets.

Input: X - pickled feature matrix
       Y - pickled label vector
       v_f - pickled validation feature matrix
       v_b - pickled validation label vector
Output: aucs - auc of the model on the validation data given a value C
'''

from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import roc_auc_score

def create_model(features, labels, c):
    model = LogisticRegression(C = hp, tol = 0.1)
    model.fit(features, labels)
    return model

def validate(model, validation_features, validation_binary):
    predicted_probs = model.predict_proba(validation_features)
    auc = roc_auc_score(validation_binary, predicted_probs[:, 0]) # confidence for class 1
    return auc	

def score(model, validation_features, validation_binary):
    return model.score(validation_features, validation_binary)

def save_model(model):
    joblib.dump(model, 'LogReg.pkl')

print 'loading datasets'
X = joblib.load('X.pkl')
Y = joblib.load('Y.pkl')
v_X = joblib.load('v_X.pkl')
v_Y = joblib.load('v_Y.pkl')

Cs = [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
aucs = []
for c in Cs:
  print 'creating model with C: ' + c
  model = create_model(X, Y, c)
  aucs.append(validate(model, v_X, v_Y))

print Cs
print aucs
print 'creating best model'
model = create_model(X, Y, Cs[aucs.index(max(aucs))])
save_model(model)

auc = validate(model, v_X, v_Y)
correct = score(model, v_X, v_Y)
print 'best auc: ' + str(auc)
print 'best score:' + str(correct)
