import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Paths
PROCESSED_PATH = "data/processed/fifa22_clean.csv"
MODEL_PATH = "models/model.pkl"

os.makedirs("backend", exist_ok=True)

print("📥 Loading processed dataset...")
df = pd.read_csv(PROCESSED_PATH)

# Features and target
X = df[["pace", "shooting", "passing", "dribbling", "defending", "physic"]]
y = df["Role"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
print("⚡ Training Decision Tree...")
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, MODEL_PATH)
print(f"💾 Model saved to {MODEL_PATH}")
