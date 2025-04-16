import sys
import os
import pandas as pd
import pickle
from exception import CustomException

class CustomCropData:
    """
    Collects user input and converts it into a pandas DataFrame.
    """
    def __init__(self, state, district, crop, crop_year, season, area):
        self.state = state
        self.district = district
        self.crop = crop
        self.crop_year = crop_year
        self.season = season
        self.area = area

    def get_data_as_data_frame(self):
        try:
            data_dict = {
                "State": [self.state],
                "District": [self.district],
                "Crop": [self.crop],
                "Crop_Year": [self.crop_year],
                "Season": [self.season],
                "Area": [self.area]
            }

            return pd.DataFrame(data_dict)

        except Exception as e:
            raise CustomException(e, sys)


class CropPredictPipeline:
    """
    Loads the trained model and preprocessor and performs prediction.
    """
    def __init__(self):
        try:
            model_path = os.path.join('artifacts', 'model.pkl')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)

            with open(preprocessor_path, 'rb') as preprocessor_file:
                self.preprocessor = pickle.load(preprocessor_file)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, input_df):
        try:
            # Transform the input using the preprocessor
            processed_data = self.preprocessor.transform(input_df)

            # Predict using the trained model
            prediction = self.model.predict(processed_data)

            return prediction

        except Exception as e:
            raise CustomException(e, sys)
