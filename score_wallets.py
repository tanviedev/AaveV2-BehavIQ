# score_wallets.py
import pandas as pd
from feature_engg import generate_features
from credit_scoring import assign_credit_score

print("\U0001F4E5 Loading transaction data...")
df = pd.read_json("data/user-wallet-transactions.json") 
print(f"✅ Loaded {len(df)} records")

print("⚙️ Generating features...")
features_df = generate_features(df)
print("🔎 Raw input:", len(df), "rows")
print("✅ After cleaning:", len(features_df), "rows remain")

print("🔍 Action counts:")
print(df['action'].value_counts())

print("📊 Feature dataframe preview:")
print(features_df.head())

print("⚖️ Assigning credit scores...")
features_df['credit_score'] = features_df.apply(assign_credit_score, axis=1)

features_df.to_csv("wallet_credit_scores.csv", index=False)
print("✅ Credit scores saved to 'wallet_credit_scores.csv'")
