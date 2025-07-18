# debug.py

import pandas as pd

# Load the merged CSV (change path if needed)
df = pd.read_csv("data/final_wallet_data_with_scores.csv")

# Print column names
print("📋 Column Names:")
for col in df.columns:
    print(f"- {col}")
