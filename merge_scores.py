# src/merge_with_scores.py
import pandas as pd

# Load the original JSON file
original_df = pd.read_json("data/user-wallet-transactions.json")

# Load the credit score CSV
score_df = pd.read_csv("data/wallet_credit_scores.csv")

# Merge on 'userWallet'
merged_df = original_df.merge(score_df[['userWallet', 'credit_score']], on='userWallet', how='left')

# Save to final_outputs
merged_df.to_csv("data/final_wallet_data_with_scores.csv", index=False)

print("✅ Merged file saved as 'final_outputs/final_wallet_data_with_scores.csv'")
