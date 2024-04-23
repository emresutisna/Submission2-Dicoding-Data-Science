import joblib
 
model = joblib.load("model/gboost_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Dropout, Graduate, or Enrolled)
    """
    # Prediksi dengan mengambil probabilitas dari model
    probabilities = model.predict_proba(data)

    # Mendapatkan kelas dengan probabilitas tertinggi
    predicted_class_index = probabilities.argmax()
    predicted_class = result_target.inverse_transform([[predicted_class_index]])[0]
    
    # Mengembalikan hasil prediksi dan probabilitasnya
    return predicted_class, probabilities[0][predicted_class_index]