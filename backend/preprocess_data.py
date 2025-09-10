import pandas as pd
import os

RAW_PATH = "data/raw/fifa22.csv"
PROCESSED_PATH = "data/processed/fifa22_clean.csv"

os.makedirs("data/processed", exist_ok=True)

print("📥 Loading raw dataset...")
df = pd.read_csv(RAW_PATH)

# -------------------------
# Select useful features
# -------------------------
features = ["pace", "shooting", "passing", "dribbling", "defending", "physic", "player_positions"]
df = df[features]

# -------------------------
# Map positions → Roles
# -------------------------
def map_role(pos):
    if "GK" in pos:
        return "Goalkeeper"
    elif any(p in pos for p in ["CB", "LB", "RB", "LWB", "RWB", "SW"]):
        return "Defender"
    elif any(p in pos for p in ["CDM", "CM", "CAM", "LM", "RM"]):
        return "Midfielder"
    elif any(p in pos for p in ["ST", "CF", "LW", "RW", "LF", "RF"]):
        return "Forward"
    else:
        return "Other"

df["Role"] = df["player_positions"].apply(map_role)

# Drop uncommon positions
df = df[df["Role"] != "Other"]

# Save processed dataset
df.to_csv(PROCESSED_PATH, index=False)
print(f"✅ Processed dataset saved to {PROCESSED_PATH}")
print(df.head())
