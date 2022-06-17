from pathlib import Path
from datetime import datetime

date = datetime.now().strftime('%d-%m-%y')

root_path = Path('E:\Coding\Ping-Logger-And-Grapher')
archive = root_path / 'Archive'
output = root_path / 'output.txt'
dated_output = archive / f'{date}.txt'

archive.mkdir(exist_ok=True)
output.rename(dated_output)
