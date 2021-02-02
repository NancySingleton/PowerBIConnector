import requests
import json
from config import get_config, get_strava_credentials

config = get_config()
strava_credentials = get_strava_credentials()

response = requests.post(
                    url = config['strava_endpoints']['token_URL'],
                    data = {
                            'client_id': strava_credentials['client_id'],
                            'client_secret': strava_credentials['client_secret'],
                            'code': strava_credentials['temp_code'],
                            'grant_type': 'authorization_code'
                            }
                )
                
strava_tokens = response.json()

with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)