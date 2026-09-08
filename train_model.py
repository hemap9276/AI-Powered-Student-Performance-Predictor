import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("student_data.csv")

# Input features
X = data[["Hours_Studied", "Previous_Score", "Attendance"]]

# Target value
y = data["Final_Score"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Machine Learning model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)

print("Model trained successfully!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save the trained model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as student_model.pkl")
