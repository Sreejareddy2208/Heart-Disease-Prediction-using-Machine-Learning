❤️ HEART DISEASE PREDICTION DASHBOARD
A Flask-based machine learning web application that predicts the likelihood of heart disease using multiple ML algorithms. This project provides an interactive UI for users to submit medical details and get predictions along with model accuracy and classification reports.

ABOUT

This project uses the Heart Disease UCI dataset to train and evaluate multiple machine learning models. The backend is written in Python and the interface is built using Flask. Users can interact through a clean UI to input medical data and receive a prediction.

FEATURES

• Predicts heart disease likelihood
• Supports multiple machine learning models
• Displays classification report for selected model
• User-friendly HTML/CSS interface
• Logging enabled
• Modular code structure

ALGORITHMS USED

This project includes 10 machine learning algorithms:

Logistic Regression

K-Nearest Neighbors (KNN)

Gaussian Naive Bayes

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

Gradient Boosting Classifier

AdaBoost Classifier

XGBoost Classifier

Extra Trees Classifier (Optional)

Each model is evaluated using accuracy score and classification report.

TECH STACK

Backend: Python, Flask
ML Libraries: pandas, numpy, scikit-learn, seaborn, matplotlib, xgboost
Frontend: HTML, CSS
Logging: Python logging module
Dataset: heart.csv

PROJECT STRUCTURE

app.py
main.py
heart.csv
templates/
index.html
static/
style.css
logs/
README (this file)
requirements.txt

GETTING STARTED

Install required packages:
pip install -r requirements.txt

Run training script:
python main.py

Start the Flask application:
python app.py

Visit:
http://127.0.0.1:5000

USAGE

Open the web app in the browser

Enter patient medical information

Select a machine learning model

Click "Predict"

View model output and evaluation

MODEL EVALUATION

Each model displays:

• Accuracy
• Precision
• Recall
• F1-score
• Classification report

This allows you to compare models easily.
