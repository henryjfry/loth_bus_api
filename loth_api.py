import requests
import json
import pprint

'''
def get_timetable(stop_id: int, api_key: str):
	"""
	Fetch the 7-day timetable for a given bus stop from the TFE Open Data API.

	Args:
		stop_id (int): The bus stop ID (e.g., 36235979)
		api_key (str): Your TFE API key

	Returns:
		dict | None: The JSON response if successful, or None if the request fails.
	"""
	url = f"https://tfe-opendata.com/api/v1/timetables/{stop_id}"
	headers = {"Authorization": f"Token {api_key}"}
	
	response = requests.get(url, headers=headers)
	
	if response.status_code == 200:
		return response.json()
	else:
		print(f"Request failed: {response.status_code} - {response.text}")
		return None
'''

import requests

BASE_URL = "https://tfe-opendata.com/api/v1"
HEADERS = {
    "Authorization": "Token YOUR_API_TOKEN"
}

def get_stops():
    """
    Fetches all bus and tram stops.
    No parameters required.
    """
    url = f"{BASE_URL}/stops"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_services():
    """
    Fetches all services (bus and tram).
    No parameters required.
    """
    url = f"{BASE_URL}/services"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_timetable(stop_id):
    """
    Fetches the timetable for a specific stop.
    @param stop_id: int - The SMS code of the stop.
    """
    url = f"{BASE_URL}/timetables/{stop_id}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_journeys(service_name):
    """
    Fetches all journeys for a specific service.
    @param service_name: str - The name of the bus or tram service (e.g., '1', 'T50').
    """
    url = f"{BASE_URL}/journeys/{service_name}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_stop_to_stop_timetable(start_stop_id, finish_stop_id, date, duration):
    """
    Fetches timetable between two stops.
    @param start_stop_id: int - The stop ID where the journey starts.
    @param finish_stop_id: int - The stop ID where the journey ends.
    @param date: int - UNIX timestamp for the start time.
    @param duration: int - Duration in minutes (max 120).
    """
    url = f"{BASE_URL}/stoptostop-timetable/?start_stop_id={start_stop_id}&finish_stop_id={finish_stop_id}&date={date}&duration={duration}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_service_status():
    """
    Fetches current service disruptions.
    No parameters required.
    """
    url = f"{BASE_URL}/status"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_live_vehicle_locations():
    """
    Fetches real-time vehicle positions.
    No parameters required.
    """
    url = f"{BASE_URL}/vehicle_locations"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_live_bus_times(stop_id):
    """
    Fetches live departure times for a specific stop.
    @param stop_id: int - The SMS code of the stop.
    """
    url = f"{BASE_URL}/live_bus_times/{stop_id}"
    response = requests.get(url, headers=HEADERS)
    return response.json()



response = get_live_bus_times(36290151)
#pprint.pprint(response)
#pprint.pprint(response)

bus_tracker_url = 'http://ws.mybustracker.co.uk/?module=json&function=getBusTimes&key=4d32a91d0e86221c6693f2309a66149d&nb=4&stopId=' + str(36290151)
response = requests.get(bus_tracker_url, headers=HEADERS)
response_json = json.loads(response.text)
#pprint.pprint(response_json)


for i in response_json['busTimes']:
	print_out1 = {
	'nameService': i['nameService'],
	'stopName': i['stopName'],
	'stopId': i['stopId'],
	'serviceDisruption': i['serviceDisruption'],
	'serviceDiversion': i['serviceDiversion'],
	'busStopDisruption': i['busStopDisruption'],
	'globalDisruption': i['globalDisruption'],
	'mnemoService': i['mnemoService'],
	'operatorId': i['operatorId'],
	'refService': i['refService']
	}
	#print(print_out1)
	for j in i['timeDatas']:
		#del j['refDest'], j['busId'], j['journeyId'], j['terminus']
		print_out = {'nameDest': j['nameDest'], 'day': j['day'], 'time': j['time'], 'minutes': j['minutes']}
		print(print_out)
	print_out1['nameDest'] = j['nameDest']
	print(print_out1)
exit()

url = 'https://tfe-opendata.com/api/v1/live_bus_times/36290151'

url = 'https://tfe-opendata.com/api/v1/stops'
api_key = 'YOUR_SERVER_TOKEN'
headers = {"Authorization": f"Token {api_key}"}
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)
for i in response_json['stops']:
	if 'Foot' in str(i['name']) or 'Walk' in str(i['name']):
		print(i)
exit()


timetable = get_timetable(36235979, "YOUR_SERVER_TOKEN")
if timetable:
	print(timetable)

