import myfitnesspal
import pandas as pd
from config import get_config, get_mfp_credentials
from datetime import date
from dateutil.rrule import rrule, DAILY

config = get_config()

def remove_extra_cols(nutrition_history):
    required_cols = config["nutrition_data"]
    nutrition_history = nutrition_history[required_cols]
    return nutrition_history
    
def get_nutrition_history():
    mfp_credentials = get_mfp_credentials()
    client = myfitnesspal.Client(mfp_credentials['username'], password=mfp_credentials['password'])

    # get start and end dates
    s = config['get_nutrition_history_from']
    start_date = date(s['year'], s['month'], s['day'])
    end_date = date.today()

    nutrition_history = pd.DataFrame()

    for dt in rrule(DAILY, dtstart=start_date, until=end_date):
        day = client.get_date(dt.strftime("%Y"),dt.strftime("%m"),dt.strftime("%d"))
        totals = day.totals
        totals['date'] = dt
        nutrition_history = nutrition_history.append(totals,ignore_index=True)

    nutrition_history = remove_extra_cols(nutrition_history)
    return nutrition_history
    
def get_weight_history():
    mfp_credentials = get_mfp_credentials()
    client = myfitnesspal.Client(mfp_credentials['username'], password=mfp_credentials['password'])
    
    weight_history = pd.DataFrame(columns = ["date", "weight"])

    s = config['get_weight_history_from']
    start_date = date(s['year'], s['month'], s['day'])

    r = client.get_measurements('Weight', start_date)
    r = list(r.items())
    
    for i in range(len(r)):
        weight_history.loc[i] = [r[i][0], r[i][1]]             
    
    return weight_history    