import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'email_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# spliting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(y_test)

# training the multiple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print('\n', np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
print(y_pred)
y_pred_round = []
for ele in y_pred:
    if ele >= 0.5:
        y_pred_round.append(1)
    else:
        y_pred_round.append(0)

print(y_pred_round)