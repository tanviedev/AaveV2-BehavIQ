import pandas as pd

def assign_credit_score(row):
    score = 500  # base score

    # Positive signals
    score += min(row['repay_ratio'], 1.0) * 300
    score += max(min(row['activity_span_days'], 365), 0) * 0.1
    score += max(min(row['net_flow'], 10000), 0) * 0.01

    # Penalties
    score -= row['liquidation_count'] * 50
    if row['repay_ratio'] < 0.5:
        score -= 100
    if row['total_borrowed'] > 0 and row['total_repaid'] == 0:
        score -= 200

    return int(max(min(score, 1000), 0))

# Load data
df = pd.read_csv('data/wallet_data.csv')

# Apply scoring
df['credit_score'] = df.apply(assign_credit_score, axis=1)

# Save results
df.to_csv('wallets_with_credit_score.csv', index=False)

print("✅ Credit scores calculated and saved to 'wallets_with_credit_score.csv'")
