import joblib

def predict(data):
    rf = joblib.load('rf_model.sav')
    return reg.predict(data)