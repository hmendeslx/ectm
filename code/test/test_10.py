# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
import pickle
import csv

# Importing the dataset
dataset = pd.read_csv('../../data/test_data/error_test_data_10.csv')

# ==================================

# ==================================
#               noise
# ==================================

X_noise_data = dataset.loc[:, ['month', 'noise']]
X_noise = X_noise_data.values

# Encoding categorical data
labelencoder_X_noise = LabelEncoder()
X_noise[:, 0] = labelencoder_X_noise.fit_transform(X_noise[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_noise = onehotencoder.fit_transform(X_noise).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_noise = np.delete(X_noise, dummies, 1)

# Loading and fitting the regression model
with open('../models/noise.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_noise = regressor.predict(X_noise)
y_pred_noise[y_pred_noise > 0.99] = 1
y_pred_noise[y_pred_noise < 0] = 0

dataset['fp_noise'] = y_pred_noise

# ==================================
#               EGT
# ==================================

X_egt_data = dataset.loc[:, ['month', 'egt']]
X_egt = X_egt_data.values

# Encoding categorical data
labelencoder_X_egt = LabelEncoder()
X_egt[:, 0] = labelencoder_X_egt.fit_transform(X_egt[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_egt = onehotencoder.fit_transform(X_egt).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_egt = np.delete(X_egt, dummies, 1)

# Loading and fitting the regression model
with open('../models/egt.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_egt = regressor.predict(X_egt)
y_pred_egt[y_pred_egt > 0.99] = 1
y_pred_egt[y_pred_egt < 0] = 0

dataset['fp_egt'] = y_pred_egt

# ==================================
#               FF
# ==================================

X_ff_data = dataset.loc[:, ['month', 'ff']]
X_ff = X_ff_data.values

# Encoding categorical data
labelencoder_X_ff = LabelEncoder()
X_ff[:, 0] = labelencoder_X_ff.fit_transform(X_ff[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_ff = onehotencoder.fit_transform(X_ff).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_ff = np.delete(X_ff, dummies, 1)

# Loading and fitting the regression model
with open('../models/ff.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_ff = regressor.predict(X_ff)
y_pred_ff[y_pred_ff > 0.99] = 1
y_pred_ff[y_pred_ff < 0] = 0

dataset['fp_ff'] = y_pred_ff

# ==================================
#               N1
# ==================================

X_n1_data = dataset.loc[:, ['month', 'n1']]
X_n1 = X_n1_data.values

# Encoding categorical data
labelencoder_X_n1 = LabelEncoder()
X_n1[:, 0] = labelencoder_X_n1.fit_transform(X_n1[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_n1 = onehotencoder.fit_transform(X_n1).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_n1 = np.delete(X_n1, dummies, 1)

# Loading and fitting the regression model
with open('../models/n1.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_n1 = regressor.predict(X_n1)
y_pred_n1[y_pred_n1 > 0.99] = 1
y_pred_n1[y_pred_n1 < 0] = 0

dataset['fp_n1'] = y_pred_n1

# ==================================
#               N2
# ==================================

X_n2_data = dataset.loc[:, ['month', 'n2']]
X_n2 = X_n2_data.values

# Encoding categorical data
labelencoder_X_n2 = LabelEncoder()
X_n2[:, 0] = labelencoder_X_n2.fit_transform(X_n2[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X_n2 = onehotencoder.fit_transform(X_n2).toarray()

# Avoiding dummy variable trap
categories = [0]
dummies = []
dummies_sum = 0

for category in categories:
    dummies_sum += (dataset.iloc[:, category].unique().size) * category
    dummies.append(dummies_sum)

X_n2 = np.delete(X_n2, dummies, 1)

# Loading and fitting the regression model
with open('../models/n2.pkl', 'rb') as f:
    regressor = pickle.load(f)

# Predicting the results
y_pred_n2 = regressor.predict(X_n2)
y_pred_n2[y_pred_n2 > 0.99] = 1
y_pred_n2[y_pred_n2 < 0] = 0

dataset['fp_n2'] = y_pred_n2

# ==================================
#        Failure Probability
# ==================================

X_data = dataset.iloc[:, 1:12]
X = X_data.values

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

# Loading and fitting the regression model
with open('../models/total_fp.pkl', 'rb') as f:
    regressor = pickle.load(f)
    
# Predicting the results
y_pred = regressor.predict(X)
y_pred[y_pred < 0] = 0
y_pred[np.where(y_pred >= 0.98)[0][0]: ] = 1

dataset['total_fp'] = y_pred

# Writing to csv file
dataset.to_csv('../../data/test_data/error_test_data_10.csv', index=False)

# ==================================

# Importing normal dataset
normal_dataset = pd.read_csv('../../data/normal_data.csv')
X_normal = normal_dataset
y_normal = normal_dataset.loc[:, 'total_fp'].values
y_normal[y_normal > 1] = 1

# Plotting graph
plt.figure(figsize=(20, 15))
plt.plot(X_data['month'][0:60], y_normal[0:60], color = 'green', linestyle='-', marker='.', label='Age under normal conditions')
plt.plot(X_data['month'][0:60], y_pred.ravel(), color = 'blue', linestyle='-', marker='.', label='Predicted age under abnormal conditions')
plt.axvline(x=np.where(y_pred==1)[0][0]+1, color='red', label='Predicted Failure Month')
plt.axvline(x=np.where(y_normal==1)[0][0]+1, color='orange', label='Normal Failure Month')        
plt.xticks(np.arange(1, 62, 2))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.title('Age (in months) vs Probability of Failure')
plt.legend(loc='best')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()
plt.savefig('../../outputs/test_10.png')

# Writing output to a new csv file

#output_df = pd.DataFrame()
#output_df['Components'] = ['Fan Blades', 'EGT', 'Fuel Flow', 'Low Pressure Fan (N1)', 'High Pressure Rotor (N2)', 'Turbine']
#output_df['Actual life span under normal conditions(in months)'] = [str(np.where(X_normal['fp_noise'].values==100)[0][0]), str(np.where(X_normal['fp_egt'].values==100)[0][0]), str(np.where(X_normal['fp_ff'].values==100)[0][0]), str(np.where(X_normal['fp_n1'].values==100)[0][0]), str(np.where(X_normal['fp_n2'].values==100)[0][0]), str(np.where(X_normal['failure_prob'].values==100)[0][0]+1)]            
#output_df['Predicted life span after sudden increase(in months)'] = [str(np.where(y_pred_noise==100)[0][0]), str(np.where(y_pred_egt==100)[0][0]), str(np.where(y_pred_ff==100)[0][0]), str(np.where(y_pred_n1==100)[0][0]), str(np.where(y_pred_n2==100)[0][0]), str(np.where(y_pred==1)[0][0])]  
#output_df['Actual value under normal conditions'] = [str(np.where(X_normal['fp_noise'].values==100)[0][0]), str(np.where(X_normal['fp_egt'].values==100)[0][0]), str(np.where(X_normal['fp_ff'].values==100)[0][0]), str(np.where(X_normal['fp_n1'].values==100)[0][0]), str(np.where(X_normal['fp_n2'].values==100)[0][0]), str(np.where(X_normal['failure_prob'].values==100)[0][0]+1)]            
#output_df['Predicted value after sudden increase'] = [str(np.where(X_normal['fp_noise'].values==100)[0][0]), str(np.where(X_normal['fp_egt'].values==100)[0][0]), str(np.where(X_normal['fp_ff'].values==100)[0][0]), str(np.where(X_normal['fp_n1'].values==100)[0][0]), str(np.where(X_normal['fp_n2'].values==100)[0][0]), str(np.where(X_normal['failure_prob'].values==100)[0][0]+1)]            
