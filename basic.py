print("Integration of k8s with jenkins and github")

print("==========================")

print("Configured by Aditya Kumar")

import pandas
import numpy
from sklearn.linear_model import LinearRegression
db = pandas.read_csv('data2.csv')
type(db)
y = db["marks"]
# Target and dependent variable
x = db["hrs"]
# feature and independent variable
mind = LinearRegression()
x = x.values
x = x.reshape(5, 1)
# exp : model : Linear function
# w : weight  / coeffiecient
mind.fit(x , y)
mind.predict([[ 6 ]])