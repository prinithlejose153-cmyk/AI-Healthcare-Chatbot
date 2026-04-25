import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Load dataset
df = pd.read_csv("dataset/training_data.csv")

# 🔥 IMPORTANT: Check columns
print("Columns:", df.columns)

# Target column (must be 'prognosis')
if "prognosis" not in df.columns:
    raise Exception("Dataset must contain 'prognosis' column")

# Features
X = df.drop("prognosis", axis=1)

# Target
y = df["prognosis"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 🔥 Ensure all features are numeric
X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(0)

# Train model
model = RandomForestClassifier()
model.fit(X, y_encoded)

# Save model + encoder
dump(model, "model/random_forest.joblib")
dump(le, "model/label_encoder.joblib")

print("✅ Model + encoder trained successfully!")