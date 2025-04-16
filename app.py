import sys
import os
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import logging

# Extend sys path for custom imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from exception import CustomException # type: ignore
from pipelines.prediction_pipeline import CustomCropData, CropPredictPipeline # type: ignore

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Home page route
@app.route('/')
def index():
    return render_template('index.html')


# Prediction route
@app.route('/predict_crop', methods=['GET', 'POST'])
def predict_crop():
    if request.method == 'GET':
        return render_template('crop_form.html')
    else:
        try:
            # Extract form data
            data = CustomCropData(
                state=request.form.get('state'),
                district=request.form.get('district'),
                crop=request.form.get('crop'),
                crop_year=int(request.form.get('crop_year')),
                season=request.form.get('season'),
                area=float(request.form.get('area'))
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            logger.info(f"Received input DataFrame:\n{pred_df}")

            # Prediction pipeline
            predict_pipeline = CropPredictPipeline()
            results = predict_pipeline.predict(pred_df)

            logger.info(f"Prediction results: {results}")

            return render_template('crop_form.html', results=results[0] if results else "Prediction failed.")
        
        except Exception as e:
            logger.exception("Error during prediction:")
            return render_template('crop_form.html', results="An error occurred during prediction. Please check inputs and try again.")
            

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
