# Aave V2 - BehavIQ ## Behavioral Wallet Clustering and Credit Scoring
## "The IQ of Behavior Meets the Future of Finance"

## 📌Project Overview
This project analyzes user behavior on the Aave V2 protocol and scores wallets based on action patterns using unsupervised clustering and rule-based credit scoring.
📊 [View Full Behavioral Analysis & Scoring Methodology](analysis.md)

## 💡Problem Statement
To score wallets based on their behavioral patterns such as deposits, borrows, liquidations, etc., by analyzing on-chain transaction data.

## Project Summary

- **Dataset:** Raw JSON data (~87MB) from Aave V2 protocol
- **Goal:** Cluster wallets based on unique transaction behaviors
- **Tech Stack:** Python, pandas, NumPy, scikit-learn, Matplotlib, seaborn
- **Output:** Cluster-labeled wallets, visual analytics, behavior insights

---

## Methodology
1. **Data Preprocessing**: Loaded Aave V2 JSON data, parsed and normalized transaction logs.
2. **Feature Engineering**: Extracted per-wallet statistics like total amount borrowed, deposit frequency, number of liquidations, action diversity, etc.
3. **Clustering**: Used KMeans to segment wallet behaviors into logical groups (Dormant, Moderate Borrowers, etc.)
4. **Scoring**: Defined a rule-based scoring strategy (0–1000) based on behavioral and cluster features.
5. **Visualization**: Generated plots for clusters, score distribution, and activity patterns.

## 🧠 Cluster Descriptions

| Cluster Type       | Behavior Summary                                               |
|--------------------|----------------------------------------------------------------|
| Dormant            | Minimal activity; 1 unique action only                         |
| Moderate Borrowers | Most organic behavior; 2–3 unique actions, varied activity     |
| Power Users        | Focused, high-frequency but narrow usage (1 action type)       |
| High Risk          | One-type action, possibly exploit-driven or automated wallets |

---

## 🚀 Potential Extensions

- Build a predictive model to classify wallets early
- Detect outlier wallets per cluster
- Score wallets for risk or engagement
- Monitor cluster evolution over time

---

## ✨ Credits

- **Data Source:** Aave V2 Protocol
- **Author:** Tanvi Takle
- **Tools:** Python, pandas, sklearn, seaborn, Matplotlib

---

## 📬 Contact

Feel free to connect if you're interested in DeFi analytics, behavioral ML, or collaborative research!

