import json

def get_config():
    with open('config.json') as config_file:
        config = json.load(config_file) 
    return config
    
def get_strava_credentials():
    config = get_config()
    strava_credentials = config['strava_credentials']
    return strava_credentials