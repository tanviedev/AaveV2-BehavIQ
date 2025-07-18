import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load clustered data
df = pd.read_csv("data/wallet_clusters.csv")

# Ensure 'plots/' folder exists
os.makedirs("data/plots", exist_ok=True)

# Optional: Rename clusters to descriptive labels
# Define your own based on your domain insights
cluster_labels = {
    0: "Dormant",
    1: "Moderate Borrowers",
    2: "Power Users",
    3: "High Risk",
    4: "Occasional Users"
}
df["cluster_label"] = df["cluster"].map(cluster_labels)

# Plot 1: Credit Score Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x="cluster_label", y="credit_score", data=df, palette="Set3")
plt.title("Credit Score Distribution by Cluster Type")
plt.xlabel("Cluster Type")
plt.ylabel("Credit Score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("data/plots/cluster_credit_score_dist.png")
plt.close()

# Plot 2: Activity Span in Days
plt.figure(figsize=(10, 6))
sns.boxplot(x="cluster_label", y="activity_span_days", data=df, palette="Set2")
plt.title("Activity Span Distribution by Cluster Type")
plt.xlabel("Cluster Type")
plt.ylabel("Activity Span (days)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("data/plots/cluster_activity_span_dist.png")
plt.close()

# Plot 3: Average Credit Score by Cluster
plt.figure(figsize=(10, 6))
avg_credit_score = df.groupby("cluster_label")["credit_score"].mean().reset_index()
sns.barplot(x="cluster_label", y="credit_score", data=avg_credit_score, palette="muted")
for index, row in avg_credit_score.iterrows():
    plt.text(index, row["credit_score"] + 1, round(row["credit_score"], 1), ha='center', fontsize=10)
plt.title("Average Credit Score by Cluster Type")
plt.xlabel("Cluster Type")
plt.ylabel("Average Credit Score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("data/plots/cluster_avg_credit_score.png")
plt.close()

# Plot 4: Unique Actions Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x="cluster_label", y="unique_actions", data=df, palette="coolwarm")
plt.title("Unique Actions per Wallet by Cluster Type")
plt.xlabel("Cluster Type")
plt.ylabel("Unique Actions")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("data/plots/cluster_unique_actions_dist.png")
plt.close()

print("✅ Enhanced cluster analysis complete. All plots saved in 'plots/' folder.")
