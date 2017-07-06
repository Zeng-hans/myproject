import os
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import wget
import zipfile
import pandas as pd


def download_if_needed(url, filename):
    """
    download from URL to filename, unless already exists
    """
    if os.path.exists(filename):
        print  "already exists"
    else:
        wget.download(url)

def get_pronto_data():
    """
    download pronto-data, unless already download
    """
    download_if_needed("https://s3.amazonaws.com/pronto-data/open_data_year_one.zip",
    "open_data_year_one.zip")

def get_trip_data():
    """
    Fetch pronto-data and extract trips as dataframe
    """
    get_pronto_data()
    zp = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zp.open('2015_trip_data.csv')
    return pd.read_csv(file_handle)

def get_weather_data():
    """
    Fetch pronto-data and extract weathers as dataframe
    """
    get_pronto_data()
    zp = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zp.open('2015_weather_data.csv')
    return pd.read_csv(file_handle)
