import joblib

def predict(data):
      model = joblib.load('reg_model.sav')
      prediction = model.predict(data)
      return prediction
