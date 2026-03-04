import csv
from pathlib import Path
from datetime import datetime

from matplotlib import pyplot as plt


def date_object(t):
    return datetime.strptime(t, '%c').strftime('%H:%M')


root_path = Path(__file__).parent
archive = root_path / 'Archive'

list_of_files = [p for p in archive.iterdir() if p.is_file() and p.suffix == '.txt']

plt.style.use('fivethirtyeight')

for file in list_of_files:
    times = []
    average_ping = []
    cloud_cover = []
    with file.open(mode='r', encoding='utf-8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            times.append(date_object(row[0]))
            average_ping.append(int(row[1]))
            cloud_cover.append(int(row[2]))
    plt.plot(times, average_ping, marker=".", label=file.stem)

plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Average Ping")
plt.title("Average Ping over a Day")
plt.legend()
plt.tight_layout()
plt.savefig(archive / 'compiled data.png')
