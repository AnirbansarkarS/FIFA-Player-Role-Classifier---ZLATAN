# backend/predict.py
import pandas as pd
import numpy as np

def predict_role(model, player_data):
    """
    Predicts the role of a player using trained model.
    player_data: Pandas Series (row from dataset)
    """
    # Features the model was trained on
    feature_cols = ["Pace", "Shooting", "Passing", "Dribbling", "Defending", "Physical"]
    
    X = player_data[feature_cols].values.reshape(1, -1)

    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    # Convert to dictionary
    probabilities = {cls: round(prob*100, 2) for cls, prob in zip(model.classes_, proba)}

    return prediction, probabilities
