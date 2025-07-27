import pandas as pd
import datetime

def compute_features(transactions):
    total_deposited = 0
    total_borrowed = 0
    total_repaid = 0
    liquidation_count = 0
    timestamps = []

    for tx in transactions:
        method = tx.get('functionName', '').lower()
        value = float(tx['value']) / 1e18
        timestamps.append(int(tx['timeStamp']))

        if 'deposit' in method:
            total_deposited += value
        elif 'borrow' in method:
            total_borrowed += value
        elif 'repay' in method:
            total_repaid += value
        elif 'liquidate' in method:
            liquidation_count += 1

    if timestamps:
        days_active = (max(timestamps) - min(timestamps)) / (60 * 60 * 24)
    else:
        days_active = 0

    net_flow = total_deposited - total_borrowed
    repay_ratio = total_repaid / total_borrowed if total_borrowed > 0 else 0

    return pd.Series({
        'total_deposited': total_deposited,
        'total_borrowed': total_borrowed,
        'total_repaid': total_repaid,
        'liquidation_count': liquidation_count,
        'activity_span_days': days_active,
        'net_flow': net_flow,
        'repay_ratio': repay_ratio
    })

def process_transactions(pkl_file="raw_transactions.pkl"):
    df = pd.read_pickle(pkl_file)
    features = df['transactions'].apply(compute_features)
    result = pd.concat([df['wallet_id'], features], axis=1)
    result.to_csv("engineered_features.csv", index=False)
    print("✅ Saved engineered_features.csv")

# For standalone running
if __name__ == "__main__":
    process_transactions()
