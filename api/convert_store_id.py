import pandas as pd

# converting every store_id into int in each csv

def convert_store_id():
    store = pd.read_csv('store.csv', dtype={'store_id': 'object'})
    store_status = pd.read_csv('store_status.csv', dtype={'store_id': 'object'})
    store_hours = pd.read_csv('store_hours.csv', dtype={'store_id': 'object'})

    store['store_id'] = store['store_id'].astype(str)
    store_status['store_id'] = store_status['store_id'].astype(str)
    store_hours['store_id'] = store_hours['store_id'].astype(str)

    store.to_csv('store.csv', index=False)
    store_status.to_csv('store_status.csv', index=False)
    store_hours.to_csv('store_hours.csv', index=False)

