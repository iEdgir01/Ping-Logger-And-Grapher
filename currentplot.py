from matplotlib import pyplot as plt
import csv
import os
from pathlib import Path
from datetime import datetime


def date_object(time):
    do = datetime.strptime(time, '%c')
    return do.strftime('%H:%M')


time = []
average_ping = []
cloud_cover = []
date = datetime.now().strftime('%d-%m-%y')

with open('E:\Coding\Ping-Logger-And-Grapher/output.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(date_object(row[0]))
        average_ping.append(int(row[1]))
        cloud_cover.append(int(row[2]))

plt.plot(time, average_ping, marker=".", label=f'{date}')
plt.xticks(rotation=45)
plt.style.use('fivethirtyeight')
plt.xlabel("Time")
plt.ylabel("Average Ping")
plt.title(f"Average Ping over {date}")
plt.legend()
plt.tight_layout()
plt.show()
