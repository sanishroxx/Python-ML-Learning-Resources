# these all codes are jupyter notebook
import numpy as np # pet name numpy
import pandas as pd # super module of numpy
import seaborn as sns # data virsual isation
import matplotlib.pyplot as plt # plot graph
%matplotlib inline # jupyter

house=pd.readd_csv('housedata.csv')

print("house")

house.columns

house.head(2)

house.tail(2)

house.Price.head(2).sum()

house[['Price','Area']]

plt.scatter(house.Area,house.Price,Price,
            color="red",marker="+")


from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(house['Area'],house.Price)

lr.intercept_ #c

lr.coef_   #m

lr.predict([[5000]])


#y = mx+c
 (o/p of m *1000)+ o/p of c


 plt.xlabel("Area in sq ft")
 plt.ylabel("Price($)")
 plt.scatter(house.Area,house.Price,color='red',marker='+')
 plt.plot(house.price,lr.predict(house[['Price]]))


                                        
