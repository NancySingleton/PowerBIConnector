import pandas as pd
import requests
import json
from config import get_config, get_strava_credentials
from strava_tokens import get_strava_tokens

config = get_config()
strava_credentials = get_strava_credentials() 

def get_page(page):
    strava_tokens = get_strava_tokens()
    access_token = strava_tokens['access_token'] 
    
    url = config['strava_endpoints']['activities_URL']
    
    r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
    r = r.json()    
    
    return r

def remove_extra_cols(activities):
    required_cols = config["activities_data"]
    activities = activities[required_cols]
    return activities
    
def get_activity_list():
    activities = pd.DataFrame()
    page = 1
    
    while True:
        r = get_page(page)
        
        if (not r):
            break
            
        for activity in r:
            activities = activities.append(activity,ignore_index=True)

        page += 1
    
    activities = remove_extra_cols(activities)
    return activities