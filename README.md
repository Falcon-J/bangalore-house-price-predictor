# Bangalore House Price Predictor

A machine learning web application that predicts house prices in Bangalore based on location, square footage, and other parameters using Ridge Regression.

## Features

- Predicts house prices in Bangalore
- Interactive web interface built with Flask
- Uses Ridge Regression model for accurate predictions
- Supports various locations across Bangalore
- Input validation and error handling

## Tech Stack

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- pickle

## Dataset

The model is trained on the Bangalore House Price Dataset containing the following features:

- Location
- Total Square Footage
- Number of BHK (Bedrooms, Hall, Kitchen)
- Number of Bathrooms

link : https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/bangalore-house-price-predictor.git
cd bangalore-house-price-predictor
```

2. Install required packages:

```bash
pip install flask scikit-learn pandas numpy pickle-mixin
```

3. Run the application:

```bash
python main.py
```

The application will be available at `http://localhost:5001`

## Usage

1. Open the web interface in your browser
2. Select the location from the dropdown
3. Enter the total square footage
4. Specify the number of BHK
5. Enter the number of bathrooms
6. Click "Predict" to get the estimated price

## Project Structure

```
├── main.py              # Flask application
├── train_model.py       # Model training script
├── RidgeModel.pkl      # Trained model
├── Cleaned_data.csv    # Processed dataset
├── templates/          # HTML templates
│   └── index.html     # Web interface
└── README.md
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Deployment on Render

1. Create a [Render](https://render.com) account
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Fill in the deployment details:
   - Name: bangalore-house-price-predictor
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`
5. Click "Create Web Service"

The application will be deployed and available at your Render URL.
