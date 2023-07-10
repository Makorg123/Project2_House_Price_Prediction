import joblib

def predict(data):
      model = joblib.load('rf_model.sav')
      prediction = model.predict(data)
      return prediction