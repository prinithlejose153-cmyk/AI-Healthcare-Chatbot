# 🧠 AI Healthcare Chatbot

A production-ready AI-powered healthcare assistant that predicts diseases based on user symptoms using Machine Learning and serves responses via a Flask backend.

---

## 🚀 Features

* 🧾 Symptom-based disease prediction
* 🤖 Machine Learning model (Random Forest Classifier)
* 🌐 REST API built with Flask
* 📊 Data-driven predictions using medical dataset
* ⚡ Fast and real-time response system
* 🧩 Modular project structure (backend + ML separation)

---

## 🏗️ Tech Stack

* **Backend:** Flask
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Model Storage:** Joblib
* **Language:** Python

---

## 🧠 How It Works

```text
User Input (Symptoms)
        ↓
Flask Backend API
        ↓
ML Model (Random Forest)
        ↓
Prediction Output
        ↓
Response to User
```

---

## 📂 Project Structure

```
AI-Healthcare-Chatbot/
│
├── app.py                 # Flask backend application
├── train_model.py         # ML model training script
├── dataset/               # Training dataset
├── model/                 # Saved ML model + encoder
├── templates/             # HTML templates
├── static/                # CSS, JS, assets
├── classes/               # Helper classes
├── instance/              # Database storage
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/prinithlejose153-cmyk/AI-Healthcare-Chatbot.git
cd AI-Healthcare-Chatbot
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

---

### 3. Activate environment

```bash
# Windows
.\venv\Scripts\Activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Train the model

```bash
python train_model.py
```

---

### 6. Run the application

```bash
python app.py
```

---

### 7. Open in browser

```
http://127.0.0.1:5000
```

---

## 📡 API Example

### POST /predict

```json
{
  "symptoms": ["itching", "skin_rash"]
}
```

### Response

```json
{
  "prediction": "Fungal infection"
}
```

---

## 📸 Preview

*(Add a screenshot here later for better impact)*

```
assets/screenshot.png
```

---

## 🎯 Future Improvements

* 🤖 Generative AI integration (LLM explanations)
* 📚 RAG-based medical knowledge system
* ☁️ Cloud deployment (AWS / Render)
* 📱 Frontend upgrade (React)
* 🔐 Authentication system

---

## 📌 Key Highlights

* Real-world ML + Backend integration
* Clean modular architecture
* Production-oriented design
* Recruiter-ready project structure

---

## 👨‍💻 Author

**N. Lejose Prinith**
📍 Hyderabad, India

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
