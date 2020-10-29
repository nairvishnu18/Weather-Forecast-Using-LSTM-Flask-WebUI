import pandas as pd
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator
import matplotlib.pyplot as plt
import pickle


# Read the Excel Dataset
excel_files = pd.read_excel('WindspeedBombay.xlsx')

# Convert it to CSV Format 
data_csv = excel_files.to_csv('WindspeedBombay.csv',index=None,header=True)


data = pd.read_csv('WindspeedBombay.csv')

temp = data['WindSpeedKmph'].values
temp = temp.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(temp))

temp_train_data = temp[:split]
temp_test_data = temp[split:]


date_train = data['Date'][:split]
date_test = data['Date'][split:]



look_back = 15

train_generator = TimeseriesGenerator(temp_train_data, temp_train_data, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(temp_test_data, temp_test_data, length=look_back, batch_size=1)

from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(
    LSTM(10,
        activation='relu',
        input_shape=(look_back,1))
)
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 100
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)



pickle.dump(model,open('mumbai-windspeed-model.pkl','wb'))

