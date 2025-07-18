import pandas as pd

def extract_amount(x):
    """Safely extract amount from actionData dict"""
    try:
        return float(x.get("amount", 0))
    except Exception:
        return 0.0

def generate_features(df):
    # Filter relevant actions
    valid_actions = ['deposit', 'borrow', 'repay', 'liquidation']
    df = df[df['action'].isin(valid_actions)].copy()

    if df.empty:
        return pd.DataFrame(columns=[
            'userWallet', 'total_deposited', 'total_borrowed', 'total_repaid',
            'liquidation_count', 'activity_span_days', 'net_flow', 'repay_ratio'
        ])

    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['amount'] = df['actionData'].apply(extract_amount)

    grouped = df.groupby('userWallet')

    features = pd.DataFrame()
    features['total_deposited'] = grouped.apply(lambda g: g[g['action'] == 'deposit']['amount'].sum())
    features['total_borrowed'] = grouped.apply(lambda g: g[g['action'] == 'borrow']['amount'].sum())
    features['total_repaid'] = grouped.apply(lambda g: g[g['action'] == 'repay']['amount'].sum())
    features['liquidation_count'] = grouped.apply(lambda g: (g['action'] == 'liquidation').sum())

    first_tx = grouped['timestamp'].min()
    last_tx = grouped['timestamp'].max()
    features['activity_span_days'] = (last_tx - first_tx).dt.days + 1

    features['net_flow'] = features['total_deposited'] - features['total_borrowed']
    features['repay_ratio'] = features['total_repaid'] / (features['total_borrowed'] + 1e-6)

    features.reset_index(inplace=True)
    return features
