# 🏠 Real Estate Price Predictor

A Flask + Machine Learning web app that predicts real estate prices based on features like bedrooms, bathrooms, square footage, and location.

---

## 🚀 Features
- Predict house price using ML model (Linear Regression / Random Forest).
- User‑friendly web interface built with Flask.
- Input fields: bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, year built, etc.
- Deployed on Render (free hosting).

---

## 📂 Project Structure
real-estate-price-predictor/
│── app.py              # Flask main app
│── model.pkl           # Trained ML model
│── requirements.txt    # Dependencies
│── Procfile            # For deployment
│── templates/          # HTML files
│── static/             # CSS/JS assets
│── README.md           # Project documentation

Code

---

## ⚙️ Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/alpi10pal-a11y/real-estate-price-predictor.git
   cd real-estate-price-predictor
Install dependencies:

bash
pip install -r requirements.txt
Run locally:

bash
python app.py
Open in browser:

Code
http://127.0.0.1:5000
🌐 Deployment
Hosted on Render free plan

Live Demo: https://real-estate-price-predictor.onrender.com (real-estate-price-predictor.onrender.com in Bing)

Start command:

bash
gunicorn app:app
📊 Dataset
Based on King County House Sales dataset (Seattle, USA).

Features include bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, year built, etc.

👨‍💻 Author
Alpi Pal

Aspiring Data Scientist | Full‑Stack Developer

📧 alpi10.pal@gmail.com

✅ License
This project is licensed under the MIT License.
