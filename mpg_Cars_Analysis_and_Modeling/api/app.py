import numpy as np
import pickle
import pandas as pd
from sys import path
import os

#path.append(os.path.realpath('../'))
from functions.check_input_data import origin_verify

filename = 'trained_model.sav'
#path_model = os.path.join(os.path.dirname(__file__), '..', 'models', filename)
#loaded_model = pickle.load(open(path_model, 'rb'))

#Creating a function for prediction
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
