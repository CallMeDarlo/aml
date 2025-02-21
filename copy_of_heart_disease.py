# -*- coding: utf-8 -*-
"""Copy of heart_disease.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hNh9jMz91fV5p4nS35cmgvgrdQDo39oU
"""

#Dataset is from  https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df=pd.read_csv("/content/heart_cleveland_upload (2).csv")
df.head(5)

df.info()

df.isnull().sum()

df.describe()

# 0 means the person does not have heart disease
# 1 means the person has heart disease
df['target'].value_counts()

#Getting target variable

target=df['target']
target

#Getting dataframe of feature variables
x=df.drop(columns='target',axis=1)
x

x_train, x_test, y_train, y_test = train_test_split(x,target,test_size=0.2,random_state=10)

# Model Implementation (LOGISTIC REGRESSION)

model=LogisticRegression()

model.fit(x_train,y_train)

#Checking accuracy of the model

pred=model.predict(x_train)
accuracy=accuracy_score(pred,y_train)
print("Accuracy on training data : ",accuracy)

pred=model.predict(x_test)
accuracy=accuracy_score(pred,y_test)
print("Accuracy on testing data : ",accuracy)

#Confusion Matrix and Classification Report

matrix=confusion_matrix(pred,y_test)
print("Confusion Matrix : \n",matrix)
class_report = classification_report(pred,y_test)
print("Classification Report : \n",class_report)

"""Custom Prediction Model"""

data=(64,1,0,110,211,0,2,144,1,1.8,1,0,0)
arr=np.asanyarray(data)
arr=arr.reshape(1,-1)

prediction=model.predict(arr)

if(prediction[0]==0):
    print("The person does not have a Heart Disease")
else:
    print("The person has a heart disease")