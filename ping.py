from os import popen
from datetime import datetime
import pyowm 


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
    weather = pyowm.OWM('2cec423cc25d56788741c6f0caa3ca9a')
except pyowm.exceptions.api_call_error.APICallTimeoutError:
    weather = 0
we = get_cloud_cover(weather)
for ip in ip_list:
    response = popen(f"ping {ip}").read()
    now = datetime.now()
    f.write(f"{','.join(format_output(now, response, we))}\n")
