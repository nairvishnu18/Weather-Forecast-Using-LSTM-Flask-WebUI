import pickle
import pandas as pd
import numpy as np
import keras
from keras.preprocessing.sequence import TimeseriesGenerator
import matplotlib.pyplot as plt

model = pickle.load(open('model.pkl','rb'))


data = pd.read_csv('Prediction-Dataset-Weather-2009-2020.csv')

data = data.drop([4138])

data['Date'] = pd.to_datetime(data['Date'])   #TO Remove Time Assosciated with date

print(data)


# Train and Test Spllit
temp = data['Average of tempC'].values
temp = temp.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(temp))

temp_train_data = temp[:split]
temp_test_data = temp[split:]

date_train = data['Date'][:split]
date_test = data['Date'][split:]

print(len(temp_train_data))
print(len(temp_test_data))


look_back = 15

train_generator = TimeseriesGenerator(temp_train_data, temp_train_data, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(temp_test_data, temp_test_data, length=look_back, batch_size=1)

prediction = model.predict_generator(test_generator)

temp_train_data = temp_train_data.reshape((-1))
temp_test_data = temp_test_data.reshape((-1))
prediction = prediction.reshape((-1))

print(temp_test_data[:10])
print(prediction[:10])


# Plotting
plt.figure(figsize=(10, 5))
plt.plot(temp_test_data,color="green")
plt.plot(prediction,color="red")
plt.xticks(temp_test_data,"")
plt.show()