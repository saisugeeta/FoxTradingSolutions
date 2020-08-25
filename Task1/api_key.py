# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:56:10 2020

@author: Sugeeta
"""


# -*- coding: utf-8 -*-
import configparser
# Getting the api key from config.ini
def api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']