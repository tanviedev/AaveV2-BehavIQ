# generate_clustering_features.py

import pandas as pd

# Load merged data
df = pd.read_csv("data/final_wallet_data_with_scores.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Basic grouping
agg = df.groupby("userWallet").agg({
    "credit_score": "first",
    "timestamp": ["min", "max", "count"],
    "action": pd.Series.nunique,
    "protocol": pd.Series.nunique,
    "network": pd.Series.nunique
})

# Flatten column names
agg.columns = [
    "credit_score",
    "first_txn", "last_txn", "total_txns",
    "unique_actions", "unique_protocols", "unique_networks"
]

# Add activity span in days
agg["activity_span_days"] = (agg["last_txn"] - agg["first_txn"]).dt.days + 1

# Reset index for userWallet
agg.reset_index(inplace=True)

# Save features
agg.to_csv("data/clustering_features.csv", index=False)
print("✅ Saved features for clustering to data/clustering_features.csv")
