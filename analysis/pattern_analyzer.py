import pandas as pd
import numpy as np
from user_management.user_profile import UserProfile
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class PatternAnalyzer:
    def __init__(self, new_keyboard_file="processed_data/keyboard_data_clean.csv", 
                 new_mouse_file="processed_data/mouse_data_clean.csv"):
        self.keyboard_data = pd.read_csv(new_keyboard_file)
        self.mouse_data = pd.read_csv(new_mouse_file)
        self.model = RandomForestClassifier()

    def train_model(self):
        # Combine keyboard and mouse data for training
        X = self.keyboard_data.drop('label', axis=1)  # Features
        y = self.keyboard_data['label']  # Target variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Make predictions
        predictions = self.model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy * 100:.2f}%")

    def predict(self, new_data):
        return self.model.predict(new_data)