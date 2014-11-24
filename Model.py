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

from sklearn import LogisticRegression
from sklearn.externals import joblib
from sklearn import roc_auc_score

def create_model(features, labels):
    model = LogisticRegression()
    model.fit(features, labels)
    return model

def validate(model, validation_features, validation_binary, validation_weights):
    predicted_probs = model.predict_proba(validation_features)
    auc = roc_auc_score(validation_binary, predicted_probs[:, 0], sample_weight = validation_weights, average = 'weighted')
    return auc

def save_model(model):
    joblib.dump(model, 'LogReg.pkl')

if __name__ == '__main__':
    X = joblib.load('X.pkl')
    y = joblib.load('y.pkl')
    model = create_model(X, y)
    save_model(model)

    v_f = joblib.load('v_f.pkl')
    v_b = joblib.load('v_b.pkl')
    v_w = joblib.load('v_w.pkl')
    auc = validate(model, v_f, v_b, v_w)
    print "auc is: " + auc