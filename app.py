import streamlit as st
import pandas as pd
import joblib

# Load model
MODEL_PATH = "models/model.pkl"
clf = joblib.load(MODEL_PATH)

st.set_page_config(page_title="⚽ FIFA Player Role Classifier", layout="centered")
st.title("⚽ FIFA Player Role Classifier")
st.write("Enter player stats to predict whether the player is a **Forward, Midfielder, Defender, or Goalkeeper**.")

# Sidebar for inputs
st.header("Player Stats Input")
pace = st.slider("Pace", 0, 100, 50)
shooting = st.slider("Shooting", 0, 100, 50)
passing = st.slider("Passing", 0, 100, 50)
dribbling = st.slider("Dribbling", 0, 100, 50)
defending = st.slider("Defending", 0, 100, 50)
physic = st.slider("Physical", 0, 100, 50)

# Prepare input
input_data = pd.DataFrame([{
    "pace": pace,
    "shooting": shooting,
    "passing": passing,
    "dribbling": dribbling,
    "defending": defending,
    "physic": physic
}])

# Predict
if st.button("Predict Role"):
    prediction = clf.predict(input_data)[0]
    probabilities = clf.predict_proba(input_data)[0]

    st.subheader("🎯 Prediction Result")
    st.success(f"Predicted Role: **{prediction}**")

    # Show probabilities
    prob_df = pd.DataFrame({
        "Role": clf.classes_,
        "Probability": probabilities
    }).sort_values(by="Probability", ascending=False)

    st.bar_chart(prob_df.set_index("Role"))
