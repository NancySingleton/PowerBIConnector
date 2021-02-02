import requests
import json
import time
from config import get_config, get_strava_credentials

def get_strava_tokens():
    with open('strava_tokens.json') as strava_tokens_file:
        strava_tokens = json.load(strava_tokens_file)   
    return strava_tokens
    
def overwrite_strava_tokens(new_strava_tokens):
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(new_strava_tokens, outfile)     
    
def refresh_strava_tokens():
    config = get_config()
    strava_credentials = get_strava_credentials()
    strava_tokens = get_strava_tokens()

    if strava_tokens['expires_at'] < time.time():
        # request new token
        response = requests.post(
                            url = config['strava_endpoints']['token_URL'],
                            data = {
                                    'client_id': strava_credentials['client_id'],
                                    'client_secret': strava_credentials['client_secret'],
                                    'grant_type': 'refresh_token',
                                    'refresh_token': strava_tokens['refresh_token']
                                    }
                        )
        new_strava_tokens = response.json()
        overwrite_strava_tokens(new_strava_tokens)