import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

# print(os.getcwd())
# print(__file__)
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))

fileloc = os.path.dirname(__file__)+'/car.data'
df = pd.read_csv(fileloc)
# print(df.head())

req_head = [['buying', 'maint', 'safety'], ['class']]

X = df[req_head[0]].values
y = df[req_head[1]]

# print(X, y)


# converting the features(X) - the string data to integer using encoder
le = LabelEncoder()
for i in range(len(X[0])):
    X[:,i] = le.fit_transform(X[:,i])

# converting the response(y) - using mapping
label_mapping = {
    'unacc': 0,
    'acc': 1,
    'good': 2,
    'vgood': 3,
}

y['class'] = y['class'].map(label_mapping)

# print(y)


# creating the model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)

print("Actuals: ", list(y_test['class']))
print("Predictions: ", list(y_pred))
print("Accuracy: ", accuracy)