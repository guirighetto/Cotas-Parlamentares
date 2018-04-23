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
import data_munging as dm

INSERT_MONGO = False

data_path = "../data/"
collection_name = "cotasParlamentares"
connection = pymongo.MongoClient("mongodb://127.0.0.1:27017")
database = "DB_593c8adece386d5cfd0caf7b"
db = connection[database]

if(INSERT_MONGO):
    dm.insert_data_mongodb(db, collection_name, data_path)

df = dm.load_data_mongodb(db, collection_name)


print(df)