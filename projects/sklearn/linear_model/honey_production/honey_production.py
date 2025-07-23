import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())
prod_per_year = df.groupby(['year']).totalprod.mean().reset_index() 
print(prod_per_year)
X = prod_per_year['year']
print(X)
X = X.values.reshape(-1,1)
print(X)
y = prod_per_year['totalprod']
print(y)
plt.scatter(X,y)
plt.show()
linear = linear_model.LinearRegression()
linear.fit(X, y)
print(linear.coef_)
print(linear.intercept_)
y_predict = linear.predict(X)
plt.plot(X, y_predict)
plt.show()
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1,1)
future_predict = linear.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()