# Run: pip install pandas scikit-learn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample hiring dataset (age, experience, gender, hired)
data = pd.DataFrame(
    {
        "age": [25, 30, 22, 40, 35, 28, 26],
        "experience": [2, 5, 1, 10, 7, 3, 4],
        "gender": ["M", "M", "F", "M", "F", "F", "M"],
        "hired": [1, 1, 0, 1, 0, 1, 1],
        # 1 = Hired, 0 = Not Hired
    }
)

# Train AI Model
X = data.drop("hired", axis=1)
y = data["hired"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier()
model.fit(X_train, y_train)


# Function to check if AI hiring decisions are biased
def check_bias(candidate):
    prediction = model.predict(candidate)
    return "Fair Hiring Decision" if prediction == 1 else "Possible Bias Detected"


# Test with a female candidate
test_candidate = pd.DataFrame({"age": [29], "experience": [4], "gender": ["F"]})
print(check_bias(test_candidate))
