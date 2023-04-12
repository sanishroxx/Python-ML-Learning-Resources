import numpy as np 
import pandas as pd
import seaborn as sns
import  mataplotib.pyplot as plt
%matplotlib inline


prince=pd.read_csv('housedata.csv')

prince.corr()


sns.heatmap(prince.corr(),annot=True)



sns.displot(prince['Price'])


from sklearn.model_selection import train_test_split



x=prince[['Area']]
y=prince['Price']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.9)

x_test

y_test


from sklearn.linear_model import  LinearRegression

lr=LinearRegression()
lr.fit(x_test,y_test)


lr.intercept_

lr.coef_

lr.predivt([[5000]])


