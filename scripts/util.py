#!/usr/bin/python3
# coding: utf-8

# --------------------------------------------------------------------------
# Library of useful functions
# --------------------------------------------------------------------------
import calendar
import datetime
import json
import os
import sys

import numpy as np
import pandas as pd
import pymongo
import pytz


def __set_max_day_month(year, month):
        """
        Function vectorizable
        Parameters Example: df["name_column"].dt.year.values, df["name_column"].dt.month.values
        """
        if(np.isnan(year) or np.isnan(month)):
            return None
        day = calendar.monthrange(year, month)[1]
        dt = pytz.timezone('America/Sao_Paulo').localize(datetime.datetime(int(year), int(month), int(day)))
        hours = int(abs(dt.utcoffset().total_seconds() / 60 / 60))
        return datetime.datetime(int(year), int(month), int(day), int(hours))

def __set_day(year, month, day):
    """
    Function vectorizable
    Parameters Example: df["name_column"].dt.year.values, df["name_column"].dt.month.values, day
    """
    if(np.isnan(day) or np.isnan(year) or np.isnan(month)):
        return None
    dt = pytz.timezone('America/Sao_Paulo').localize(datetime.datetime(int(year), int(month), int(day)))
    hours = int(abs(dt.utcoffset().total_seconds() / 60 / 60))
    return datetime.datetime(int(year), int(month), int(day), int(hours))

__set_max_day_month = np.vectorize(__set_max_day_month)
__set_day = np.vectorize(__set_day)

def date_munging(df, day=None, month=None, year=None):
    """
    Parameters
        df : Serie of type datetime
        day : None = Original day of the series
                "max" = Last day of the month
                Some value = The day set in the parameter

        month : None = Original month of the series
                Some value = The month set in the parameter

        year : None = Original year of the series
                Some value = The year set in the parameter

        Example : data_munging(df["dateRef"],1)
                    data_munging(df["dt_vigencia"],15, 6)
                    data_munging(df["dt_vigencia"],"max")
    """
    if(year == None):
        year_func = df.dt.year.values
    else:
        year_func = year

    if(month == None):
        month_func = df.dt.month.values
    else:
        month_func = month

    if(day == None):
        day_func = df.dt.day.values
    elif(day == "max"):
        return __set_max_day_month(year_func, month_func)
    else:
        day_func = day

    return __set_day(year_func, month_func, day_func)
