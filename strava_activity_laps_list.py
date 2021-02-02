import pandas as pd
import requests
import json
from config import get_config, get_strava_credentials
from strava_tokens import get_strava_tokens

config = get_config()
strava_credentials = get_strava_credentials() 

def get_activity_details(activity_id):
    strava_tokens = get_strava_tokens()
    access_token = strava_tokens['access_token'] 
    
    url = config['strava_endpoints']['activities_URL']
    
    r = requests.get(url + '/' + str(activity_id) + '?access_token=' + access_token)
    r = r.json()    
    
    return r

def remove_extra_cols(activity_laps_list):
    required_cols = config["activity_laps_data"]
    activity_laps_list = activity_laps_list[required_cols]
    return activity_laps_list
    
def get_activity_laps_list(activity_list):
    activity_laps_list = pd.DataFrame()
    activity_count = config['get_laps_for_last_x_activities']
    
    for i in range(activity_count):
        activity_id = activity_list.loc[i,'id']
        activity_details = get_activity_details(activity_id)
        activity_laps = activity_details.get('laps')
    
        for j in range(len(activity_laps)):
            activity_laps[j]['activity_id'] = activity_id
            activity_laps_list = activity_laps_list.append(activity_laps[j],ignore_index=True)

    activity_laps_list = remove_extra_cols(activity_laps_list)
    return activity_laps_list