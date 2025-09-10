# FIFA-Player-Role-Classifier---ZLATAN
# ⚽

A machine learning + Streamlit project that predicts a football player’s **role** (Forward, Midfielder, Defender, Goalkeeper) based on their in-game FIFA attributes such as **pace, shooting, passing, dribbling, defending, and physicality**.

---

## 📌 Features

* 🎯 Predicts **player role** from 6 key stats.
* 📊 Shows prediction **probabilities** with a bar chart.
* 🖱️ Interactive **Streamlit web app** with sliders for inputs.
* 💾 Trained using a **Decision Tree Classifier** on FIFA dataset.

---

## 🗂️ Project Structure

```
├── backend/
│   ├── train_model.py       # Script to train model and save model.pkl
│   ├── model.pkl            # Saved trained model
├── data/
│   ├── fifa_players.csv     # FIFA dataset (raw or cleaned)
├── app.py                   # Streamlit frontend
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone repo

```bash
git clone https://github.com/yourusername/fifa-role-classifier.git
cd fifa-role-classifier
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install requirements

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train Model

Make sure you have the dataset (`data/fifa_players.csv`). Then run:

```bash
python backend/train_model.py
```

This will create `backend/model.pkl`.

---

## 🚀 Run App

```bash
streamlit run app.py
```

Now open the link shown in the terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 🖼️ Demo

* Adjust sliders for **Pace, Shooting, Passing, Dribbling, Defending, Physicality**
* Click **Predict Role**
* See the predicted role and probability distribution

---

## 📊 Example Output

![Demo Screenshot](https://dummyimage.com/600x400/000/fff\&text=Demo+Prediction+UI)

---

## ✅ Next Improvements

* Add **dropdown** to select real players from dataset instead of manual input.
* Improve model (Random Forest, XGBoost, Neural Nets).
* Add formation analyzer (team balance).

---

💡 **Built with:**

* Python 🐍
* Streamlit
* Scikit-learn
* Pandas

---

Would you like me to also write the **`requirements.txt`** so your setup runs without missing packages?
