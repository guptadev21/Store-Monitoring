# calculating uptime and downtime of stores using data in store_status.csv and openig and closing time in store_hours.csv
from datetime import timedelta
import pandas as pd
from fastapi import FastAPI
from api.localtime_to_utc import *
from api.convert_store_id import *

app = FastAPI()

app = FastAPI()


@app.get("/trigger_report")
def trigger_report():
    # in store status timestamp is in datetime format
    # in store hours timestamp is in time format
    # calculate uptime and downtime of stores using data in store_status.csv
    convert_store_id()
    convert_timestamps()
    store_status = pd.read_csv('store_status.csv')
    store_hours = pd.read_csv('store_hours.csv')

    # store_status['timestamp_local'] = pd.to_datetime(store_status['timestamp_local'])
    # store_status['timestamp_local'] = store_status['timestamp_local'].dt.time
    
    # sort store status by day_of_week and then timestamp
    store_status = store_status.sort_values(by=['timestamp_local'])
    store_status.to_csv('store_status_filtered.csv', index=False)
    # return store's store_id from store_status
    store_id = str(store_status['store_id'].values[0])
    return store_id


@app.get("/get_report")
def get_report(store_id: int):
    store_data = pd.read_csv('store_status.csv')

    try:
        # group store_data by store_id and sort on timestamp_local
        store_data = store_data[store_data['store_id'] == store_id]
        store_data = store_data.sort_values(by=['timestamp_local'])
    except:
        return {
            "store_id": store_id,
            "data" : "Store not found"
        }
    return store_data

