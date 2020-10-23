import pickle
import pandas as pd
import numpy as np


model = pickle.load(open('model.pkl','rb'))

data = pd.read_csv('./dataset/Prediction-Dataset-Weather-2009-2020.csv')

data = data.drop([4138])

data['Date'] = pd.to_datetime(data['Date'])   #TO Remove Time Assosciated with date

# print(data)


# Train and Test Spllit
temp = data['Average of tempC'].values
# print(type(temp))
# print(temp)
temp = temp.reshape((-1))
# print(type(temp))
look_back=15

def predict(num_prediction, model):
    prediction_list = temp[-look_back:]
    # print(prediction_list)
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        # print(type(x),type(prediction_list))
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = data['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

num_prediction = 5
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)


def forecast_T():
    return forecast

def forecast_D():
    return forecast_dates
