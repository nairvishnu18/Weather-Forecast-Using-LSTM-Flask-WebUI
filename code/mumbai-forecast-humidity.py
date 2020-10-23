import pickle
import pandas as pd
import numpy as np
import csv
import warnings

warnings.filterwarnings('ignore')
model = pickle.load(open('mumbai-humid-model.pkl','rb'))

data = pd.read_csv('./dataset/mumbaihumidity.csv')


# Train and Test Spllit
temp = data['humidity'].values
# print(type(temp))
# print(temp)
temp = temp.reshape((-1))
# print(type(temp))
look_back=15

def predict(num_prediction, model):
    prediction_list = temp[-look_back:]
    print(prediction_list)
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        print(type(x),type(prediction_list))
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return (prediction_list).tolist()
    
def predict_dates(num_prediction):
    last_date = data['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

num_prediction = 5
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)


print(forecast)
print(forecast_dates)

res = dict(zip(forecast_dates, forecast))


with open('mumbai-humidity-predicted.csv','a',newline='')as f:
    fieldnames =['Date','Humidity']
    writetofile = csv.DictWriter(f,fieldnames=fieldnames)
    writetofile.writeheader()
    writer = csv.writer(f)
    for key,value in res.items():
        writer.writerow([key,value])


