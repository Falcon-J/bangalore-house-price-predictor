import pandas as pd
import pickle
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Load cleaned data
df = pd.read_csv("Cleaned_data.csv")

# Define features and target
X = df[['location', 'total_sqft', 'bath', 'bhk']]
y = df['price']  # Replace 'price' if your target column is named differently

# Preprocessing pipeline
categorical = ['location']
numerical = ['total_sqft', 'bath', 'bhk']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
    ('num', StandardScaler(), numerical)
])

# Full model pipeline
pipe = make_pipeline(preprocessor, Ridge())

# Train model
pipe.fit(X, y)

# Save model
with open("RidgeModel.pkl", "wb") as f:
    pickle.dump(pipe, f)

print("✅ Model retrained and saved using scikit-learn 1.7.x")
