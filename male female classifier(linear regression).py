
"""
Created on Fri Jul 28 07:28:18 2017

@author: abhinav
"""


from sklearn import tree as T

clf = T.DecisionTreeClassifier()

#the given data is in this order : [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']



clf = clf.fit(X, Y)
a=input('height')
b=input('weight')
c=input('shoe size')
c=43
prediction = clf.predict([[a ,b,c]])


print('the given person is a')
print(prediction)