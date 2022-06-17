from os import popen
from datetime import datetime
from os.path import join, dirname
from dotenv import dotenv_values
import pyowm 

#.env configuration
dotenv_path = join(dirname(__file__), '.env')
config = dotenv_values(dotenv_path)

def format_output(time, latency, weather):
    time = now.strftime('%c')
    latency = latency.split()[-1][:-2]
    return [time, latency, weather]


def get_cloud_cover(w):
    if not w:
        return 0
    mgr = weather.weather_manager()
    observation = mgr.weather_at_place("Durban,za")
    durban_weather = observation.weather
    cloud_cover = durban_weather.clouds
    return str(cloud_cover)


f = open("output.txt", "a+")
ip_list = ["8.8.8.8"]
try:
    weather = pyowm.OWM(config['weather_api'])
except pyowm.exceptions.api_call_error.APICallTimeoutError:
    weather = 0
we = get_cloud_cover(weather)
for ip in ip_list:
    response = popen(f"ping {ip}").read()
    now = datetime.now()
    f.write(f"{','.join(format_output(now, response, we))}\n")
