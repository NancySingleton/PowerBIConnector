# PowerBIConnector

## CREATE STRAVA CONNECTION

1) Create an app at https://www.strava.com/settings/api and note your Client_ID and Client_Secret.

2) Obtain a temp auth code by pasting the following in your browser.
http://www.strava.com/oauth/authorize?client_id=[REPLACE_WITH_YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all

   Click Authorise.
   
   You will be sent to the following URL:
   
   http://localhost/exchange_token?state=&code=[TEMP_AUTH_CODE_TO_COPY]&scope=read,activity:read_all,profile:read_all

3) Update config.json with your information:
	- Client ID
	- Client Secret
	- Temp Code
	
4) Run setup.py to generate strava_tokens.json.

5) You can now run main.py which will print your Strava data.	



## USE WITH POWER BI

1) Update 'location' in powerbiscript.py to be your local copy.

2) In Power BI, click Get Data and then Python Script. This will let you paste in the contents of a script. Paste in the contents of powerbiscript.py.