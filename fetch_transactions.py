import requests
import pandas as pd
from tqdm import tqdm

ETHERSCAN_API_KEY = "my_api_key"

def get_transactions(wallet):
    url = (
        f"https://api.etherscan.io/api?module=account&action=txlist"
        f"&address={wallet}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}"
    )
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data['status'] == '1':
            return data['result']
        else:
            return []
    except Exception as e:
        print(f"Error for {wallet}: {e}")
        return []

def main():
    wallets = pd.read_csv("data/aaveV2data.csv")
    wallets['transactions'] = [get_transactions(w) for w in tqdm(wallets['wallet_id'])]
    wallets.to_pickle("raw_transactions.pkl")
    print("✅ Saved raw_transactions.pkl")

if __name__ == "__main__":
    main()
