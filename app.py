from flask import Flask, request, render_template
import numpy as np
import pandas as pd
# Assuming PredictPipeline and CustomData are correctly implemented in the following module
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    print("Accessed the home page")
    return render_template('home.html')

# Route to handle form submissions and predictions
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    print("Prediction route accessed with method:", request.method)
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Collect data from the form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=float(request.form.get('writing_score')),
            reading_score=float(request.form.get('reading_score'))
        )
        
        print("Form Data:", data)
        
        # Convert data to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("DataFrame for prediction:", pred_df)
        
        # Predict
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        print("Prediction Results:", results)
        
        # Render the template with prediction results
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
