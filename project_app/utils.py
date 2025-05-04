import project_config
import pandas as pd
import numpy as np

import pickle
import json


class EnergyData():
    def __init__(self):
        pass

    def load_model(self):
        """
            This method will be used to loading Linear Regression Model
        """
        with open(project_config.MODEL_FILE_PATH, "rb") as f:
            self.linear_regression_model = pickle.load(f)
        
        self.feature_names = self.linear_regression_model.feature_names_in_
        return self.feature_names
    
    def load_json_data(self):
        """
            This method will be used to Load data from JSON files
            Data:
                Label Encoding Data
                OneHot Encoding Data
        """
        with open(project_config.LABEL_ENC_DATA_PATH, "r") as f:
            self.column_encoded_data = json.load(f)
        return self.column_encoded_data

    def get_data_from_user(self):
        self.load_model()
        self.load_json_data()
        Building_Type = self.data.get('Building Type')
        Square_Footage = eval(self.data['Square Footage'])
        Number_of_Occupants  = eval(self.data['Number of Occupants'])
        Appliances_Used = eval(self.data['Appliances Used'])
        Average_Temperature = eval(self.data['Average Temperature'])
        Day_of_Week = self.data['Day of Week']

        test_array = np.zeros((1,self.feature_names.size))

        test_array[0][0] = self.column_encoded_data['Building Type'][Building_Type]
        test_array[0][1] = Square_Footage
        test_array[0][2] = Number_of_Occupants
        test_array[0][3] = Appliances_Used
        test_array[0][4] = Average_Temperature
        test_array[0][5] = self.column_encoded_data['Day of Week'][Day_of_Week]
        self.df_test = pd.DataFrame(test_array, columns= self.feature_names)
        print(self.df_test)


    def predict_charges(self, data):
        self.data = data
        self.get_data_from_user()
        self.prediction = self.linear_regression_model.predict(self.df_test)[0]
        print('Predicted Price is:',np.around(self.prediction,3))
        return self.prediction
    
    def save_data_in_db(self, testing_data_collection):

        input_data = dict(self.data)
        input_data.update({'Prediction':self.prediction})
        testing_data_collection.insert_one(input_data)
        return "Sucessful"






    




