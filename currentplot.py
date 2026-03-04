import csv
from pathlib import Path
from datetime import datetime

from matplotlib import pyplot as plt


def date_object(t):
    return datetime.strptime(t, '%c').strftime('%H:%M')


root_path = Path(__file__).parent
date = datetime.now().strftime('%d-%m-%y')

times = []
average_ping = []
cloud_cover = []

plt.style.use('fivethirtyeight')

with open(root_path / 'output.txt', 'r', encoding='utf-8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        times.append(date_object(row[0]))
        average_ping.append(int(row[1]))
        cloud_cover.append(int(row[2]))

plt.plot(times, average_ping, marker=".", label=f'{date}')
plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Average Ping")
plt.title(f"Average Ping over {date}")
plt.legend()
plt.tight_layout()
plt.show()
