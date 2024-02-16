import numpy as np
import pickle
import pandas as pd
from sys import path
import os
path.append(os.path.realpath('mpg_Cars_Analysis_and_Modeling/'))
from functions.check_input_data import origin_verify
import streamlit as st

filename = 'trained_model.sav'
path_model = os.path.join(os.path.dirname(__file__), '..', 'models', filename)
loaded_model = pickle.load(open(path_model, 'rb'))

#Creating a function for prediction
def mpg_prediction(input_data):
    
    input_df = pd.DataFrame([input_data])

    # We can now pass this input to the model to make predictions.
    prediction = loaded_model.predict(input_df)

    # The output of the prediction is the predicted value
    return round(prediction[0][0], 1)

def main():
    #Giving a title for web application
    st.title('Miles Per Gallon Prediction Web App')

    #Getting the input data from the user
    cylinders = st.text_input('Number of cylinders')
    displacement = st.text_input('Displacement of the car')
    horsepower = st.text_input('Horsepower')
    weight = st.text_input('Weight of the car value')
    acceleration = st.text_input('Acceleration value')
    model_year = st.text_input('Car\'s model')
    origin = st.text_input('Origin value (1,2,3)')

    input_data = {
            'cylinders': cylinders,
            'displacement': displacement,
            'horsepower': horsepower,
            'weight': weight,
            'acceleration': acceleration,
            'model year': model_year,
            'origin' : origin
        }
    input_data = origin_verify(input_data)

    #Code for prediction
    diagnosis = ''

    if st.button('mpg Test Result'):
        mpg = mpg_prediction(input_data)
        diagnosis += str(mpg)

    st.success(diagnosis)

if __name__ == '__main__':
    main()