import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("House Price Prediction dataset.csv")

# ✅ Use only 14 features
features = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors',
            'waterfront','view','condition','sqft_above','sqft_basement',
            'yr_built','yr_renovated','city','statezip']

X = df[features]
y = df['price']

# Numeric & categorical split
numeric_features = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors',
                    'waterfront','view','condition','sqft_above','sqft_basement',
                    'yr_built','yr_renovated']
categorical_features = ['city','statezip']

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Pipeline
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model saved with 14 features")
