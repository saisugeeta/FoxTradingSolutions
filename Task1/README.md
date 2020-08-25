## INSTRUCTIONS
Kindly follow the steps below to sucessfully run the files.

1. (pre-requisite) have python3  installed.

2. To install all the packages, type

    <pre>pip install Flask</pre>
    <pre>pip install configparser</pre>
    <pre>pip install Flask-APScheduler</pre>
    <pre>pip install requests</pre>


3. Now, our job is scheduled. Now, simply run the <strong><u>app.py</u></strong> file and then open up your browser and go to [http://localhost:5000/](http://localhost:5000/) to see the webapp.

## CODE EXPLANATION
1. [https://www.kaggle.com/sahilgandhi94/indian-pincodes#](https://www.kaggle.com/sahilgandhi94/indian-pincodes#) -In here Data includes ALL pincodes mapped to the city, state and district name.This dataset was used to extract pincodes of all states in India.But used only 16 records from the state of AndhraPradesh for timebeing.

---

### The description of each function is described below.

1. 'dataset_import()' ----- imports the csv file/dataset and collects 16 records of pincodes of state AndhraPradesh

    
    

2. 'api_key()' --------- collects the api key required for extracting api from [Link](https://openweathermap.org/api) stored in congig.ani

    
    

3. 'api_extraction(zip_code)'----------Taking zip_code/pincode as the argument,formats the url and calls the api,and stores it in json.

    
    

4. 'map_creation()'-------------------This method is called by the scheduler,It creates a dictionary/map having zip code as the key,and  value which  is also a dictionary/map which has "temperature","humidity","cityname" as keys,and values for each key is extracted from the json which has been fetched by method api_extraction.

    ```
    {"zipcode":{"temperature":,"humidity":,"city_name","updated":}}
    visualizer.visualize('bubblesort', save=True, path='path/to/directory')
    ```
    Here "updated " key is used ,just to keep account of the update value in client side.And I have assumed update value for each to be set to be 1 initially.
        ```
            
        
            if zipcode_withtem[zip_code]["updated"]==1:
             zipcode_withtem[zip_code]["humidity"]=data["main"]["humidity"]
             zipcode_withtem[zip_code]["temp"]=data["main"]["temp"]
            
        ```
        So when ,client chooses update value as 0,then ' "updated":0 ' the above condition will not update the dictionary.
        
        
    
5.'request_response()'------------------ When the client changes the update value,the client makes a request to the server,sending the zip_code/pincode as the request.The server will recieve it and make the change in the dictionary/map zipcode_withtem i.e "updated":0/1 according to the change made in the client side.



6.In the client side.
        The columns made are: 
	
	
	
		    1.Zipcode/Pincode
		    2.City Name
		    3.Temperature
		    4.Humidity
		    5.Unit-A dropdown list containing C/F as options(Celcious/Farenheit).Initailly set to C
		    6.Update Value(which is initially 1)
		    7.Change Update Value-a dropdown list,where we change to 0/1.
		    
		    
		    
		    
		    
		    
            
            
            
7.When we change TO C/F,it triggers the js function onchange(),which will convert the temperature.






8.When we change the update value,the dropdown list will trigger the js function onchange_function1(),which will send 
the key and the value changed as a request to the server,and the server will respond it with a message.

        


        
