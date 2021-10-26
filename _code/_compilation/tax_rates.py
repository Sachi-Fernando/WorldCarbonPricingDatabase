#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:16:17 2021

@author: GD
"""

import pandas as pd
import glob
import os

path_prices = "/Users/gd/OneDrive - rff/Documents/Research/projects/ecp/wcpd_dataset/source_data/design_and_prices/prices/"

def prices_df(path_prices):
    
    folderList = ["Argentina", "Australia/Australia_CPM",
                  "Canada/federal/fuel_charge",
                  "Chile", "Colombia", "Denmark", "Estonia",
                  "Finland", "France", "Iceland", "Ireland", "Japan",
                  "Latvia", "Liechtenstein", "Mexico/tax", "Norway",
                  "Poland", "Portugal", 
                  "Singapore", "Slovenia", "South_Africa", "Sweden",
                  "Switzerland/tax", "Ukraine", "United_Kingdom", 
                  "Canada/provinces_territories/Alberta",
                  "Canada/provinces_territories/British_Columbia",
                  "Canada/provinces_territories/New_Brunswick", 
                  "Canada/provinces_territories/Prince_Edward_Island", 
                  "Canada/provinces_territories/Newfoundland_and_Labrador/Tax", 
                  "Canada/provinces_territories/Northwest_Territories"]

    dfList = []
    
    #each iteration of the loop will add a dataframe to the list
    for folderName in folderList:
        os.chdir(path_prices+folderName)
        fileList = glob.glob("*_tax*_prices.csv")

        for fileName in fileList:        
            df=pd.read_csv(fileName, keep_default_na=False, header=0)
            dfList.append(df)

    #'axis=0' ensures that we are concatenating vertically,
    concatDf=pd.concat(dfList,axis=0)

    return concatDf




##### Have done:
## 1. Reset default values for ETS_dummy (from None to NaN to prevent autofill)
## 2. Corrected year data type in various loops
## 3. Corrected price calculations (value)
## 4. Filled in NA if ETS_dummy is 0
## 5. Checked results for countries such as France and Finland


##### To-do:
## 1. Double-check country and state name consistency between the two sources
## 2. Fill in ETS_dummy (manually or automatically)
## 3. Fill in ETS currency code by scheme
## 4. Adjust for changes in ETS scope (Canada, China, California ...?) 
## 5. Auto fill ETS prices (change back to the right file path)
## 6. Add data that are not available in ICAP
