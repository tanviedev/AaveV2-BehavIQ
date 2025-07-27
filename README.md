# Aave V2 - BehavIQ  
## Behavioral Wallet Clustering and Credit Scoring  
### *"The IQ of Behavior Meets the Future of Finance"*

📊 [View Full Behavioral Analysis & Scoring Methodology](analysis.md)
📥 [Download Final Behavioral Wallet Scores (CSV)](./Final_Behavioral_Wallet_Scores.csv)

---

## 💡 Problem Statement

Score DeFi wallets based on behavioral patterns such as deposits, borrows, repayments, and liquidations by analyzing Aave V2 on-chain transaction data.

---

## 📁 Project Summary

- **Dataset:** Raw JSON data (~87MB) from Aave V2 protocol  
- **Goal:** Cluster wallets based on behavioral usage and assign an intelligent credit score  
- **Tech Stack:** Python, pandas, NumPy, scikit-learn, Matplotlib, seaborn  
- **Output:**  
  - Cluster-labeled wallets  
  - Scored credit profile per wallet (0–1000)  
  - Visual analytics  
  - CSV export of labeled and scored data

---

## ⚙️ Methodology

1. **Data Preprocessing**  
   - Loaded Aave V2 JSON dump  
   - Parsed and normalized logs into a structured format  

2. **Feature Engineering**  
   - Computed per-wallet stats:  
     - Total borrowed/repaid  
     - Deposit/borrow frequencies  
     - Repayment ratio  
     - Liquidation counts  
     - Unique action count  
     - Net flow (in-out funds)  
     - Activity span

3. **Clustering**  
   - Applied KMeans clustering  
   - Optimal cluster count chosen via Elbow method  
   - Used behavior-driven features to form wallet groups  

4. **Scoring (Rule-Based)**  
   - Score range: **0–1000**  
   - Formula incorporates:  
     - Repay ratio (weighted)  
     - Activity span  
     - Net inflow  
     - Liquidation penalties  
     - No repayment / default penalties  

5. **Visualization**  
   - Clustered wallet scatter plots  
   - Score distributions  
   - Time-activity heatmaps  

---

## 🧠 Cluster Descriptions

| Cluster Type       | Behavior Summary                                               |
|--------------------|----------------------------------------------------------------|
| Dormant            | Minimal activity; only 1 unique action                         |
| Moderate Borrowers | Most organic wallets; 2–3 unique actions, good repayment       |
| Power Users        | High-frequency, often single-purpose action users              |
| High Risk          | Abnormal patterns, poor repayment or frequent liquidations     |

---

## 🚀 Potential Extensions

- Predictive ML model to label new wallets early  
- Risk/engagement scoring as APIs  
- Detection of malicious or automated wallet behavior  
- Dashboard for cluster & score monitoring  

---

## ✨ Credits

- **Data Source:** Aave V2 Protocol  
- **Author:** Tanvi Takle  
- **Tools:** Python, pandas, NumPy, scikit-learn, seaborn, Matplotlib  

---

## 📬 Contact

Want to collaborate on DeFi analytics, behavioral modeling, or credit-risk ML?  
**Let’s connect!**
