from strava_tokens import refresh_strava_tokens
from get_strava_data import get_activity_list, get_activity_laps_list
from get_mfp_data import get_nutrition_history, get_weight_history

refresh_strava_tokens()
activity_list = get_activity_list()
activity_laps_list = get_activity_laps_list(activity_list)

print(activity_list)
print(activity_laps_list)

nutrition_history = get_nutrition_history()
weight_history = get_weight_history()

print(nutrition_history)
print(weight_history)