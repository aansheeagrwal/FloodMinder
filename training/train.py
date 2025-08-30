# training/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the final data
data = pd.read_csv("final_data.csv")

# Separate features and target
X = data.drop('class', axis=1)
y = data['class']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize RandomForest classifier
classifier = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state=42)

# Train the model
classifier.fit(X_train, y_train)

# Test accuracy
pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, pred)
print(f"Model trained! Accuracy on test set: {accuracy*100:.2f}%")

# Save model using joblib
joblib.dump(classifier, 'model.pickle')
print("Model saved to 'model.pickle'.")
