# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:56:38 2020

@author: Sugeeta
"""

# -*- coding: utf-8 -*-
import pandas as pd
def dataset_import():
    # A map/dictionary where the data will be stored,i.e zip_code,temperature ,humidity.which willl be sent to the client side to display.
    pin_code_dataset=pd.read_csv("pincode.csv")# Accesing the dataset
    state=["ANDHRA PRADESH"]
    dataset=pin_code_dataset.loc[pin_code_dataset["statename"].isin(state)].head(16)
    # For time being only 16 records are being taken from the state of AndhraPradesh
    return dataset

