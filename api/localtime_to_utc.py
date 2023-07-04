import pandas as pd
from datetime import datetime
from pytz import timezone

def convert_timestamps():
    store = pd.read_csv('store.csv')
    store_status = pd.read_csv('store_status.csv')

    store_status['region'] = store_status['store_id'].apply(lambda x: store.loc[store['store_id'] == x, 'timezone_str'].values[0])

    # Convert utc datetime text to datetime
    store_status['timestamp_utc'] = pd.to_datetime(store_status['timestamp_utc'])

    # Convert each timestamp to local datetime using the region
    store_status['timestamp_local'] = store_status.apply(lambda row: row['timestamp_utc'].tz_convert(timezone(row['region'])), axis=1)

    # get day of the week from local datetime
    store_status['day_of_week'] = store_status['timestamp_local'].dt.dayofweek
    store_status['day_of_week'] = store_status['day_of_week'].apply(lambda x: x % 7)

    store_status.to_csv('store_status.csv', index=False)

    # calculate total hours of store by end_time_local - start_time_local in store_hours.csv
    # columns end_time_local and start_time_local are time not datetime

    store_hours = pd.read_csv('store_hours.csv')

    # convert store_hours end_time_local and start_time_local to datetime
    store_hours['end_time_local'] = pd.to_datetime(store_hours['end_time_local'], format='%H:%M:%S').dt.time
    store_hours['start_time_local'] = pd.to_datetime(store_hours['start_time_local'], format='%H:%M:%S').dt.time

    # Calculate the time difference in seconds
    store_hours['hours'] = store_hours.apply(lambda row: (datetime.combine(datetime.min, row['end_time_local']) - datetime.combine(datetime.min, row['start_time_local'])).total_seconds() / 3600, axis=1)
    
