from flask import Flask,render_template,request
import os,csv

app = Flask(__name__)


# #Home Page
@app.route('/')
def home():
    return render_template('weather.html')


@app.route('/forecast')
def forecast():
    return render_template('newforecast.html')


# Mumbai Section begins here
# Mumbai Temp Forecast
@app.route('/getforecastmumbai',methods=['POST'])
def getforecastmumbai():
    if request.method == 'POST':
        results=[]
        rows=[]
        file_exists = os.path.exists('./Prediction/mumbai-temp-predicted.csv')
        if(file_exists):
            with open('./Prediction/mumbai-temp-predicted.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                fields = next(reader)
                for row in reader: 
                    rows.append(row) 
                for row in rows:
                        results.append({
                            "Date": row[0],
                            "Values": row[1]
                            
                            })
        else:
            results.append({
                            "Date": "No Record",
                            "Values": "Found"
                            })


    return render_template("newforecast.html", results=results)


#Mumbai Humidity
@app.route('/gethumiditymum',methods=['POST'])
def gethumiditymum():
    if request.method == 'POST':
        results=[]
        rows=[]
        file_exists = os.path.exists('./Prediction/mumbai-humidity-predicted.csv')
        if(file_exists):
            with open('./Prediction/mumbai-humidity-predicted.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                fields = next(reader)
                for row in reader: 
                    rows.append(row) 
                for row in rows:
                        results.append({
                            "Date": row[0],
                            "Values": row[1]
                            
                            })
        else:
            results.append({
                            "Date": "No Record",
                            "Values": "Found"
                            })


    return render_template("newforecast.html", results=results)

#----------END OF MUMBAI---------

# Pune Section Begins Here
# Pune Forecast Temperature
@app.route('/getforecastpune',methods=['POST'])
def getforecastpune():
    if request.method == 'POST':
        res=[]
        rows=[]
        file_exists = os.path.exists('./Prediction/pune-temp-predicted.csv')
        if(file_exists):
            with open('./Prediction/pune-temp-predicted.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                fields = next(reader)
                for row in reader: 
                    rows.append(row) 
                for row in rows:
                        res.append({
                            "Date": row[0],
                            "Values": row[1]
                            
                            })
        else:
            res.append({
                            "Date": "No Record",
                            "Values": "Found"
                            })


    return render_template("newforecast.html", res=res)


#Pune Humidity
@app.route('/gethumiditypune',methods=['POST'])
def gethumiditypune():
    if request.method == 'POST':
        res=[]
        rows=[]
        file_exists = os.path.exists('./Prediction/pune-humidity-predicted.csv')
        if(file_exists):
            with open('./Prediction/pune-humidity-predicted.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                fields = next(reader)
                for row in reader: 
                    rows.append(row) 
                for row in rows:
                        res.append({
                            "Date": row[0],
                            "Values": row[1]
                            
                            })
        else:
            res.append({
                            "Date": "No Record",
                            "Values": "Found"
                            })


    return render_template("newforecast.html", res=res)


#-----------END  OF PUNE------------ 
if __name__ == "__main__":
    app.run(debug=True)
