# Step 1: Install Required Libraries

# pip install scikit-learn pandas numpy

import pandas as pd
import numpy as np
from sklearn.model_selection import
train_test_split
from sklearn.ensemble import
RandomForestClassifier

# Load network traffic dataset
data = pd.read_csv("network_traffic.csv")

# Split features and labels
X = data.drop("attack_type", axis=1)
y = data["attack_type"]

# Train AI model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Function to detect threats
def detect_threat(new_data):
    prediction = model.predict(new_data)
    return "Alert! Potential Threat Detected!" if prediction == 1 else "No Threat Detected"

# Test with sample network traffic data
new_request = np.array([[0.2, 0.7, 0.1, 0.9]]) # Replace with real traffic data

print(detect_threat(new_request))
