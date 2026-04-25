from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd
import secrets
from joblib import load
import os

# -------------------- APP CONFIG --------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

db = SQLAlchemy(app)

# -------------------- LOAD DATA --------------------
df = pd.read_csv("dataset/training_data.csv")

# Last column should be disease
symptom_columns = df.columns[:-1]

# Load trained model
model = load("model/random_forest.joblib")

# -------------------- DATABASE MODEL --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

# -------------------- UTIL FUNCTIONS --------------------
def make_token():
    return secrets.token_urlsafe(16)

def predict_disease(user_symptoms):
    input_vector = np.zeros(len(symptom_columns))

    for symptom in user_symptoms:
        symptom = symptom.strip().lower()
        if symptom in symptom_columns:
            index = list(symptom_columns).index(symptom)
            input_vector[index] = 1

    prediction = model.predict([input_vector])[0]
    return prediction

# -------------------- ROUTES --------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def index_auth():
    session_id = make_token()
    session['id'] = session_id
    return render_template("index_auth.html", sessionId=session_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form.get("uname")
        passw = request.form.get("passw")

        user = User.query.filter_by(username=uname, password=passw).first()
        if user:
            return redirect(url_for("index_auth"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form.get('uname')
        mail = request.form.get('mail')
        passw = request.form.get('passw')

        new_user = User(username=uname, email=mail, password=passw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

# -------------------- CHAT API --------------------

user_sessions = {}

@app.route('/ask', methods=['GET'])
def chat():
    message = request.args.get("message", "").lower()
    session_id = request.args.get("sessionId")

    if not session_id:
        return jsonify({'status': 'error', 'message': 'Session ID missing'})

    state = user_sessions.get(session_id, 0)
    response = []

    if state == 0:
        response.append("Enter symptoms separated by comma (example: itching, skin_rash)")
        user_sessions[session_id] = 1

    elif state == 1:
        symptoms = message.split(",")
        disease = predict_disease(symptoms)

        response.append(f"Predicted Disease: {disease}")
        response.append(f'<a href="https://www.google.com/search?q={disease} treatment">Learn more</a>')

        user_sessions[session_id] = 2

    else:
        response.append("Session ended. Refresh to start again.")

    return jsonify({'status': 'OK', 'answer': response})

# -------------------- MAIN --------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)