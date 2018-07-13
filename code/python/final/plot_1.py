import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('../../../data/final/1.csv')
df2 = pd.read_csv('../../../data/final/3.csv')
df3 = pd.read_csv('../../../data/final/5.csv')
df4 = pd.read_csv('../../../data/final/7.csv')
df5 = pd.read_csv('../../../data/final/9.csv')
ndf = pd.read_csv('../../../data/engine_data_normal_final.csv')

fp_1 = df1['failure_prob'].values/100
fp_2 = df2['failure_prob'].values/100
fp_3 = df3['failure_prob'].values/100
fp_4 = df4['failure_prob'].values/100
fp_5 = df5['failure_prob'].values/100
fp_n = ndf['failure_prob'].values/100

months = ndf['month'].values

plt.plot(months, fp_n, color = 'green', linestyle='-', marker='.', label='Age under normal conditions - Normal')
plt.plot(months, fp_1, color = 'red', linestyle='-', marker='.', label='Age under normal conditions - 1')
plt.plot(months, fp_2, color = 'blue', linestyle='-', marker='.', label='Age under normal conditions - 3')
plt.plot(months, fp_3, color = 'black', linestyle='-', marker='.', label='Age under normal conditions - 5')
plt.plot(months, fp_4, color = 'yellow', linestyle='-', marker='.', label='Age under normal conditions - 7')
plt.plot(months, fp_5, color = 'orange', linestyle='-', marker='.', label='Age under normal conditions - 9')

plt.axvline(x=np.where(fp_n==1)[0][0]+1, color='green', label='Predicted Failure Month - Normal')
plt.axvline(x=np.where(fp_1==1)[0][0]+1, color='red', label='Predicted Failure Month - 1')
plt.axvline(x=np.where(fp_2==1)[0][0]+1, color='blue', label='Predicted Failure Month - 2')
plt.axvline(x=np.where(fp_3==1)[0][0]+1, color='black', label='Predicted Failure Month - 3')
plt.axvline(x=np.where(fp_4==1)[0][0]+1, color='yellow', label='Predicted Failure Month - 4')
plt.axvline(x=np.where(fp_5==1)[0][0]+1, color='orange', label='Predicted Failure Month - 5')

plt.xticks(np.arange(1, 62, 2))
plt.yticks(np.arange(0, 1.05, 0.05))

plt.title('Age (in months) vs Probability of Failure')
plt.legend(loc='best')
plt.xlabel('Age (in months)')
plt.ylabel('Probability of Failure')
plt.show()