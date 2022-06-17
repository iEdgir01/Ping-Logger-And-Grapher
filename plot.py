from datetime import datetime
from matplotlib import pyplot as plt
from pathlib import Path
import csv


def date_object(time):
    do = datetime.strptime(time, '%c')
    return do.strftime('%H:%M')


list_of_files = []
for path in Path('E:/Coding/Ping-Logger-And-Grapher/Archive').iterdir():
    if path.is_file():
        list_of_files.append(path)
no_of_files = len(list_of_files)

for file in list_of_files:
    time = []
    average_ping = []
    cloud_cover = []
    with file.open(mode='r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            time.append(date_object(row[0]))
            average_ping.append(int(row[1]))
            cloud_cover.append(int(row[2]))
    label = file.stem
    plt.plot(time, average_ping, marker=".", label=label)

plt.xticks(rotation=45)
plt.style.use('fivethirtyeight')
plt.xlabel("Time")
plt.ylabel("Average Ping")
plt.title("Average Ping over a Day")
plt.legend()
plt.tight_layout()
plt.savefig('E:/Coding/Ping-Logger-And-Grapher/Archive/compiled data.png')
