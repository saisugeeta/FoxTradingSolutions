# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:55:04 2020

@author: Sugeeta
"""

# -*- coding: utf-8 -*-
import requests
from api_key import api_key
#Aquiring The Api by formating the url of openweathermap,and appending the apikey 
def api_extraction(zip_code):
    apikey=api_key()
    api_url="http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=metric&appid={}".format(zip_code,"in",apikey)
    response=requests.get(api_url)
    #print(response.json())
    return response.json()

