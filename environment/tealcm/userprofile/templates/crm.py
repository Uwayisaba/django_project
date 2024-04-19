# Importing required libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sample data (replace with your dataset)
data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 35, 30, 40, 45],
    'AnnualIncome': [50000, 60000, 75000, 80000, 100000],
    'SpendingScore': [50, 60, 70, 80, 90]
})

# Selecting features for segmentation
features = ['Age', 'AnnualIncome', 'SpendingScore']
X = data[features]

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Clustering using KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualizing clusters
plt.scatter(data['AnnualIncome'], data['SpendingScore'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')
plt.show()

# Displaying cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
print('Cluster Centers:')
print(pd.DataFrame(cluster_centers, columns=features))
