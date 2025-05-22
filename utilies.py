#utilities 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.linear_model import LinearRegression


glcx = pd.read_csv('glcx.csv')


xg1 = glcx.drop('glc',axis=1)
yg1 = glcx['glc']

diab = pd.read_csv('diab.csv')



from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
diabc = diab.copy()
diabc['db_or_no'] = le.fit_transform(diabc['Class'])
diabc['polydipsia'] = le.fit_transform(diabc['Polydipsia'])
diabc['polyuria'] = le.fit_transform(diabc['Polyuria'])
diabc['vissionblurr']=le.fit_transform(diabc['Blurred Vision'])

diabc.drop('Polydipsia',axis=1,inplace=True)
diabc.drop('Polyuria',axis=1,inplace=True)
diabc.drop('Blurred Vision',axis=1,inplace=True)



diabc.drop('Class',axis=1,inplace=True)


x1 = diabc[['Age','BMI','Fasting Glucose (mg/dL)','HbA1c (%)','polydipsia','polyuria','vissionblurr']]
y1 = diabc['db_or_no']

scaler = StandardScaler()
x1 = scaler.fit_transform(x1)





