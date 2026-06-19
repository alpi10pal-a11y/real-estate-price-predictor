from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    model = None
    print("⚠️ Model file not found. Please train and save model.pkl first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', error="Model file missing. Train and save model.pkl first.")

    try:
        # Collect inputs
        data = {
            'bedrooms': int(request.form['bedrooms']),
            'bathrooms': float(request.form['bathrooms']),
            'sqft_living': int(request.form['sqft_living']),
            'sqft_lot': int(request.form['sqft_lot']),
            'floors': float(request.form['floors']),
            'waterfront': int(request.form['waterfront']),
            'view': int(request.form['view']),
            'condition': int(request.form['condition']),
            'sqft_above': int(request.form['sqft_above']),
            'sqft_basement': int(request.form['sqft_basement']),
            'yr_built': int(request.form['yr_built']),
            'yr_renovated': int(request.form['yr_renovated']),
            'city': request.form['city'],
            'statezip': request.form['statezip']
        }

        # ✅ Validation
        if data['sqft_living'] < 300 or data['sqft_living'] > 10000:
            return render_template('index.html', error="Living area must be between 300 and 10000 sqft")
        if data['sqft_lot'] < 500 or data['sqft_lot'] > 50000:
            return render_template('index.html', error="Lot size must be between 500 and 50000 sqft")
        if not data['city'].isalpha():
            return render_template('index.html', error="City must contain only letters")
        if not data['statezip'].replace(" ", "").isalnum():
            return render_template('index.html', error="State/Zip must be alphanumeric")

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=False)
