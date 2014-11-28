#!/usr/bin/env python

'''
Author: Alan Kao

Creates Logistic Regression model and validates its performances using
AUC. Requires pre-pickled datasets

Input: X - pickled feature matrix
       Y - pickled label vector
       v_f - pickled validation feature matrix
       v_b - pickled validation label vector
       v_w - pickled sample weights
Output: auc - auc of the model on the validation data
        model - pickled model
'''

from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import roc_auc_score

def create_model(features, labels):
    model = LogisticRegression()
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

X = joblib.load('X.pkl')
Y = joblib.load('Y.pkl')
model = create_model(X, Y)
save_model(model)

v_X = joblib.load('v_X.pkl')
v_Y = joblib.load('v_Y.pkl')
auc = validate(model, v_X, v_Y)
correct = score(model, v_X, v_Y)
print "auc is: " + str(auc)
print "score is: " + str(correct)
