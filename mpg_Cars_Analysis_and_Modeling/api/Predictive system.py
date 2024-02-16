import numpy as np
import pickle
import pandas as pd
import os

filename = 'trained_model.sav'
path_model = os.path.join(os.path.dirname(__file__), '..', 'models', filename)
loaded_model = pickle.load(open(path_model, 'rb'))

def origin_verify(input_data):
    if input_data['origin'] == 1:
        input_data['origin_1'] = input_data.pop('origin')
        input_data['origin_2'] = 0
        input_data['origin_3'] = 0
    elif input_data['origin'] == 2:
        input_data['origin_1'] = 0
        input_data['origin_2'] = input_data.pop('origin')
        input_data['origin_2'] = 1
        input_data['origin_3'] = 0
    else:
        input_data['origin_1'] = 0
        input_data['origin_2'] = 0
        input_data['origin_3'] = input_data.pop('origin')
        input_data['origin_3'] = 1
    return input_data

input_data = {
    'cylinders': 6,
    'displacement': 350,
    'horsepower': 100,
    'weight': 4400,
    'acceleration': 15,
    'model year': 72,
    'origin' : 2
}
input_data = origin_verify(input_data)

# We convert the input to a single-row DataFrame to have feature names
input_df = pd.DataFrame([input_data])

# We can now pass this input to the model to make predictions.
prediction = loaded_model.predict(input_df)

# The output of the prediction is the predicted value
print("mpg:", round(prediction[0][0], 1))