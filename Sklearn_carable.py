import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_excel(r"C:\Users\Laptop Supplier PH\Documents\Sklearn_supervised&unsupervised_data.xlsx", sheet_name="Sheet1")
print(df.columns)
X = df[["Study_Hours", "Attendance"]]

Y = df["Pass"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, Y_train)

prediction = model.predict(pd.DataFrame([[5,72]], columns = ["Study_Hours", "Attendance"]))

print("Prediction:", prediction)
