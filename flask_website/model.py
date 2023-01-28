import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import new_email

dataset = pd.read_csv(r'email_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# spliting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# training the multiple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

def get_result(email_data, regressor):
    email_data = np.array([email_data])
    # predicting the test set results
    y_pred = regressor.predict(email_data)
    np.set_printoptions(precision=2)

    if y_pred >= 0.5:
        return 1
    else:
        return 0
    


#####################################
# TEST
#####################################

# email = '''Hi Finnley,

# Congratulations, you have passed the screening stage for the Data Scientist (Risk Research) Intern position and will move on to the next step of the process, our technical test.

# The test will take at most 120 minutes. Please ensure you use the same email on the test as you did on your application so we can credit you with your results. You will receive an invitation from HackerRank shortly after receiving this email.

# Please ensure you take the test within 72 hours of receiving it. The system takes some time to send the test link, but if you do not receive it by the end of the day, please respond to this email, and I will re-send it.

# Any questions? Please join our internship LinkedIn Network for the fastest response time, and post your questions in the group.

# Best of luck!

# Eleanor Hawkins
# Campus Recruitment Team
# GeoComply'''

# test = new_email.email_data(email)
# print(get_result(test, regressor))