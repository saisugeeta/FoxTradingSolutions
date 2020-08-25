# -*- coding: utf-8 -*-

#importing required Libraries
from flask import Flask,render_template,request,jsonify
from flask_apscheduler import APScheduler

from createdictionary import map_creation
from dataset import dataset_import

scheduler=APScheduler()# For Scheduling Every 1 second


app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def dashboard():
    return render_template('home.html',dataframe=zipcode_withtem)

# Allows to make a request or recieve a request from server
@app.route('/request_response', methods=['GET', 'POST'])
def request_response():

    # POST request
    if request.method == 'POST':
        
        data=request.get_json(force=True)# parse as JSON
        
        key=data["key"]
        
        zipcode_withtem[str(key)]["updated"]=int(data["value"])
        
        
        
        return 'OK', 200
        

    # GET request
    else:
        message = {'Sucessfull':'From SERVER!'}
        return jsonify(message)  # serialize and use JSON headers
    
    






if __name__=="__main__":
    zipcode_withtem={}
    dataset=dataset_import()
    zipcode_withtem=map_creation(dataset,zipcode_withtem)#Invoking the function for the first time.
    
    
    #Scheduling map_creation method to run every 1 second
    scheduler.add_job(id='Scheduled task',func=map_creation,trigger='interval',seconds=1,args=[dataset,zipcode_withtem])
    scheduler.start()
    app.run(debug=True)