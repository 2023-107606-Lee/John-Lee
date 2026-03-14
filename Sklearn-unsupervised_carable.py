import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_excel(r"C:\Users\Laptop Supplier PH\Documents\Sklearn_supervised&unsupervised_data.xlsx", sheet_name = "Sheet2")

X = df[["Income", "Spending"]]

model = KMeans(n_clusters=3)
model.fit(X)

df["Cluster"] = model.labels_

print(df)
