# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:53:47 2020

@author: Sugeeta
"""

# -*- coding: utf-8 -*-
from api_extraction import api_extraction
# This function creates a map/dictonary zipcode_withtem={zipcode:{"cityname":,"temperature":,"humidity":,"updated":}}
#This is the format of map,being constructed,which can be accessed from client side.
# It uses the pincode dataset of India to access the pincodes,and name of the city/town,which will be the keys in the map/dictonary created in this function
# It will call the api_extraction function,to access the api of each pincode in the taken data set.
def map_creation(dataset,zipcode_withtem):
    
    for i in dataset.index:
        zip_code=str(dataset["pincode"][i])# Accesing the pincode from data set
        
        data=api_extraction(zip_code) # For extracting the  APi of the particular zip code
        
        if zip_code not in zipcode_withtem:
            zipcode_withtem[zip_code]={}
            zipcode_withtem[zip_code]["city_name"]=data["name"]
        if "updated" not in zipcode_withtem[zip_code]:
            zipcode_withtem[zip_code]["updated"]=1
        
        if zipcode_withtem[zip_code]["updated"]==1:#A check Condition for update functionality,Suppose if the client has changes the update value,in the map/dict zipcode_withtem,"updated"key will also be changed.
        # This condition allows to update the dictionary/map zipcode_withtem(temerature and humidity parameters),only if the value in "updated" is 1 ,otherwise it will retain the previous value,Hence controlling the update
        
            zipcode_withtem[zip_code]["humidity"]=data["main"]["humidity"]
            zipcode_withtem[zip_code]["temp"]=data["main"]["temp"]
    return zipcode_withtem
            