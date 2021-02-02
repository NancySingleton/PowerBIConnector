import pandas as pd
import requests
import json
from config import get_config, get_strava_credentials
from strava_tokens import get_strava_tokens

config = get_config()
strava_credentials = get_strava_credentials() 

def get_page_of_activities(page_number):
    strava_tokens = get_strava_tokens()
    access_token = strava_tokens['access_token'] 
    
    url = config['strava_endpoints']['activities_URL']
    
    r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page_number))
    r = r.json()    
    
    return r

def format_activity_list(activities):
    required_cols = config["activities_data"]
    activities = activities[required_cols]
    return activities
    
def get_activity_list():
    activities = pd.DataFrame()
    page_number = 1
    
    while True:
        r = get_page_of_activities(page_number)
        
        if (not r):
            break
            
        for activity in r:
            activities = activities.append(activity,ignore_index=True)

        page_number += 1
    
    activities = format_activity_list(activities)
    return activities
    
def get_activity_details(activity_id):
    strava_tokens = get_strava_tokens()
    access_token = strava_tokens['access_token'] 
    
    url = config['strava_endpoints']['activities_URL']
    
    r = requests.get(url + '/' + str(activity_id) + '?access_token=' + access_token)
    r = r.json()    
    
    return r

def format_activity_laps_list(activity_laps_list):
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

    activity_laps_list = format_activity_laps_list(activity_laps_list)
    return activity_laps_list