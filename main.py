from strava_tokens import refresh_strava_tokens
from strava_activity_list import get_activity_list
from strava_activity_laps_list import get_activity_laps_list

refresh_strava_tokens()
activity_list = get_activity_list()
activity_laps_list = get_activity_laps_list(activity_list)

print(activity_list)
print(activity_laps_list)