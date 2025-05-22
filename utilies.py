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


glcx = pd.read_csv(r'E:\py.proj-20250522T154056Z-1-001\py.proj\diabetes_aware\data\glcx.csv')


xg1 = glcx.drop('glc',axis=1)
yg1 = glcx['glc']

diab = pd.read_csv(r'E:\py.proj-20250522T154056Z-1-001\py.proj\diabetes_aware\data\diab.csv')



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

# tri accura

#do you relate method
#d
diab2 = pd.read_csv(r'E:\py.proj-20250522T154056Z-1-001\py.proj\diabetes_aware\data\combined_diabetes_dataset.csv')

diab2.head()

diab2['db_or_no'] = le.fit_transform(diab2['Class'])
diab2['polydipsia'] = le.fit_transform(diab2['Polydipsia'])
diab2['polyuria'] = le.fit_transform(diab2['Polyuria'])
diab2['vissionblurr']=le.fit_transform(diab2['Blurred Vision'])
diab2['Unexplained_weight']= le.fit_transform(diab2['Unexplained Weight Loss'])

diab2.drop('Polydipsia',axis=1,inplace=True)
diab2.drop('Polyuria',axis=1,inplace=True)
diab2.drop('Blurred Vision',axis=1,inplace=True)
diab2.drop('Unexplained Weight Loss',axis=1,inplace=True)
diab2.drop('Class',axis=1,inplace=True)
diab2.drop('Fatigue',axis=1,inplace=True)

#nd
diab3 = pd.read_csv(r'E:\py.proj-20250522T154056Z-1-001\py.proj\diabetes_aware\data\combined_diabetes_dataset.csv')



diab3['db_or_no'] = le.fit_transform(diab3['Class'])
diab3['polydipsia'] = le.fit_transform(diab3['Polydipsia'])
diab3['polyuria'] = le.fit_transform(diab3['Polyuria'])
diab3['vissionblurr']=le.fit_transform(diab3['Blurred Vision'])
diab3['Unexplained_weight']= le.fit_transform(diab3['Unexplained Weight Loss'])



diab3.drop('Polydipsia',axis=1,inplace=True)
diab3.drop('Polyuria',axis=1,inplace=True)
diab3.drop('Blurred Vision',axis=1,inplace=True)
diab3.drop('Unexplained Weight Loss',axis=1,inplace=True)
diab3.drop('Class',axis=1,inplace=True)
diab3.drop('Fatigue',axis=1,inplace=True)



x2 = diab2[['Age','BMI','Fasting Glucose (mg/dL)','HbA1c (%)','polydipsia','polyuria','vissionblurr','Unexplained_weight']]
y2 = diab2['db_or_no']

x3 = diab3[['Age','BMI','Fasting Glucose (mg/dL)','HbA1c (%)','polydipsia','polyuria','vissionblurr','Unexplained_weight']]
y3 = diab3['db_or_no']




