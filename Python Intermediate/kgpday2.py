import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline



uh=pd.read_csv('USA_Housing.csv')


uh.head()


uh.info()


uh.describe()

uh.corr() #execute this with heat

uh.columns


#after copied this output

x=uh[['Area Population','Price']]
y=uh['Price']


from sklearn.model_selection import train_test_split

train_test_split
#after executing click on the '+' symboll you will be get defination
# and copy the x value and copied x value is paste the above cell



from sklearn.linear_model import LinearRegression



lr=linearRegression()

lr.fit(x_train,y_train)


predict=lr.predict(x_test)
plt.scatter(y_test,predict)
#after executing get the output




from sklearn import matrices
matrices.mean_squared_error(y_test,predict)
np.sqrt(metrics.mean_squared_error(y_test,predict)
