# wallet_clusters.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings("ignore")

# Ensure data folder exists
if not os.path.exists("data"):
    raise FileNotFoundError("❌ 'data/' folder does not exist. Please create it and place the input files inside.")

# Load clustering features
features_path = "data/clustering_features.csv"
if not os.path.exists(features_path):
    raise FileNotFoundError(f"❌ File not found: {features_path}")
features_df = pd.read_csv(features_path)

# Fill missing credit scores with default
if 'credit_score' in features_df.columns:
    features_df['credit_score'] = features_df['credit_score'].fillna(500.0)

# Convert datetime to timestamps
for col in ['first_txn', 'last_txn']:
    if col in features_df.columns:
        features_df[col] = pd.to_datetime(features_df[col], errors='coerce')
        features_df[col] = features_df[col].astype(np.int64) // 10**9

# Select numeric features
features_numeric = features_df.select_dtypes(include=['number'])

# Handle any remaining NaNs in numeric features
features_numeric = features_numeric.fillna(features_numeric.mean())

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_numeric)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels
features_df["cluster"] = clusters

# Apply PCA for 2D visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot and save PCA cluster visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=clusters, palette="tab10", s=60, edgecolor='k')
plt.title("Wallet Clusters via PCA")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig("wallet_clusters.png")
plt.show()

# Save final dataframe
output_path = "data/wallet_clusters.csv"
features_df.to_csv(output_path, index=False)
print(f"✅ Clustering complete. Results saved to '{output_path}' and PCA plot to 'wallet_clusters.png'")
