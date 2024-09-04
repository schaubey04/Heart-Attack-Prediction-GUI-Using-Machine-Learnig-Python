import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('heart.csv')

print(heart_data.tail())

print("Shape of the dataset:", heart_data.shape)

print(heart_data.info())

print("Missing values:\n", heart_data.isnull().sum())

print("Statistical description:\n", heart_data.describe())

print("Distribution of Target Variable:\n", heart_data['target'].value_counts())

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression()

model.fit(X_train, Y_train)

train_predictions = model.predict(X_train)
training_accuracy = accuracy_score(train_predictions, Y_train)
print('Accuracy on Training data:', training_accuracy)

test_predictions = model.predict(X_test)
test_accuracy = accuracy_score(test_predictions, Y_test)
print('Accuracy on Test data:', test_accuracy)

input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)

input_data_array = np.asarray(input_data)

input_data_reshaped = input_data_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)

if prediction[0] == 0:
    print('The person does not have a Heart Disease')
else:
    print('The person has Heart Disease')
