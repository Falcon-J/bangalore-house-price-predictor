#flask, scikit-learn, pandas, numpy,pikle-mixin
from flask import Flask, request, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(BASE_DIR, 'Cleaned_data.csv'))
pipe = pickle.load(open(os.path.join(BASE_DIR, 'RidgeModel.pkl'), 'rb'))

# data=pd.read_csv('Cleaned_data.csv')  # Load your dataset here
# pipe = pickle.load(open('RidgeModel.pkl', 'rb'))  # Load your trained model here

# pipe = pickle.load(open('RidgeModel.pkl', 'rb'))  # Load your trained model here
@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if all required fields are present
        required_fields = ['location', 'total_sqft', 'bhk', 'bath']
        for field in required_fields:
            if not request.form.get(field):
                return f"Error: {field} is required", 400
        
        location = request.form.get('location')
        total_sqft = float(request.form.get('total_sqft'))
        bhk = float(request.form.get('bhk'))
        bath = float(request.form.get('bath'))

        input_data = pd.DataFrame([[location, total_sqft, bhk, bath]], 
                                columns=['location', 'total_sqft', 'bhk', 'bath'])
        prediction = pipe.predict(input_data)[0] * 1e5

        return str(round(prediction, 2))
    except ValueError as e:
        return "Error: Please ensure all numeric inputs are valid numbers", 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred during prediction", 500


if __name__ == '__main__':
    # app.run(debug=True, port=5001)
    app.run(debug=False)
    # Set debug=True for development, change to False in production
    # Change port as needed, default is 5000
# To run the application, use the command: python main.py
# Ensure you have Flask installed: pip install Flask
