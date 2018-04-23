#!/usr/bin/python3
# coding: utf-8

# --------------------------------------------------------------------------
# Import libraries
# --------------------------------------------------------------------------
import os
import time
import datetime

import numpy as np
import pandas as pd
import pymongo

import util

# --------------------------------------------------------------------------
# Data Munging
# --------------------------------------------------------------------------
def insert_data_mongodb(db, collection_name, data_path):
    """
    Parameters 
        db: database connection pymongo
        collection_name: name collection of mongodb
        data_path: Path of data directory 
    """
    for file in os.listdir(os.fsencode(data_path)):
        filename = os.fsdecode(file)
        
        if filename.endswith(".csv"):
            full_path = os.path.join(data_path, filename)

            year = filename[-8:-4]

            df = pd.read_csv(full_path, sep=";")

            df["dt_referencia"] = datetime.datetime(int(year), 1, 1)
            df["dt_referencia"] = util.date_munging(df["dt_referencia"])
    
            db[collection_name + "." + year].drop()
            db[collection_name + "." + year].insert_many(df.to_dict('records'))


def load_data_mongodb(db, collection_name):
    """
    Parameters 
        db: database connection pymongo
        collection_name: name collection of mongodb
    """
    df = pd.DataFrame()
    for i in range(2009,2018):
        df_tmp = pd.DataFrame(list(db[collection_name + "." + str(i)].find()))
        df = pd.concat([df, df_tmp], ignore_index=True)

    return df
