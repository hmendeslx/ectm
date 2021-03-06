# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Importing the dataset
dataset = pd.read_csv('../../../data/train_data/train_data.csv')

X = dataset.iloc[:, 1:12].values
y = dataset.loc[:, ['total_fp']].values

# Encoding categorical data
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X = np.delete(X, dummies, 1)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Fitting Simple Linear Regression to the Training set
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, y_train)

# Predicting the results
y_pred = regressor.predict(X_test)
y_pred[y_pred > 0.99] = 1
y_pred[y_pred < 0] = 0

# Saving the model
with open('../../../models/random_forest/rf_total_fp.pkl', 'wb') as f:
    pickle.dump(regressor, f)