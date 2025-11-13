from flask import Flask, render_template, request
from main import HEART
from sklearn.metrics import classification_report, accuracy_score

# Initialize Flask app
app = Flask(__name__)

# Load dataset and model class
data = 'heart.csv'
heart_obj = HEART(data)

# All available models
models = {
    'K-Nearest Neighbors (KNN)': heart_obj.knn_algo,
    'Logistic Regression': heart_obj.logistic_regression,
    'Naive Bayes': heart_obj.naive_bayes,
    'Decision Tree': heart_obj.Decision_Tree,
    'Random Forest': heart_obj.Random_forest,
    'AdaBoost': heart_obj.adaboost,
    'Gradient Boosting': heart_obj.gradient_boosting,
    'XGBoost': heart_obj.XGB,
    'Support Vector Machine (SVM)': heart_obj.SVC
}

# 🏠 Home route
@app.route('/')
def home():
    return render_template('index.html', models=models)

# 🚀 Prediction route (supports multiple model selection)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1️⃣ Collect patient features
        features = [float(request.form[f'feature{i}']) for i in range(1, 14)]

        # 2️⃣ Get selected models (checkbox list)
        model_choices = request.form.getlist('model')

        if not model_choices:
            return render_template('index.html', models=models, results=[])

        # 3️⃣ Map model names to trained model attributes
        model_map = {
            'K-Nearest Neighbors (KNN)': 'reg_knn',
            'Logistic Regression': 'reg_lr',
            'Naive Bayes': 'reg_nb',
            'Decision Tree': 'reg_dt',
            'Random Forest': 'reg_rf',
            'AdaBoost': 'reg_ad',
            'Gradient Boosting': 'reg_gb',
            'XGBoost': 'reg_xgb',
            'Support Vector Machine (SVM)': 'reg_svc'
        }

        results = []

        # 4️⃣ Train and evaluate each selected model
        for model_choice in model_choices:
            models[model_choice]()  # Train selected model

            # Get model instance dynamically
            reg_model = getattr(heart_obj, model_map[model_choice])

            # Predict single input
            y_pred = reg_model.predict([features])[0]

            # Evaluate accuracy and classification report
            y_test_pred = reg_model.predict(heart_obj.x_test)
            acc = accuracy_score(heart_obj.y_test, y_test_pred)
            report = classification_report(heart_obj.y_test, y_test_pred, output_dict=True)

            # Store all results
            results.append({
                'model': model_choice,
                'prediction': int(y_pred),
                'accuracy': round(acc * 100, 2),
                'report': report
            })

        # 5️⃣ Send results to frontend
        return render_template('index.html', models=models, results=results)

    except Exception as e:
        return f"⚠️ Error occurred: {str(e)}"


if __name__ == '__main__':
    print("\n✅ Server running! Open this URL in your browser:")
    print("👉 http://127.0.0.1:5000/\n")
    app.run(debug=True)
