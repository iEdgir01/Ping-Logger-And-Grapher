# Ping Logger and Grapher

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Add your OpenWeatherMap API key to a `.env` file in the project folder:
   ```
   weather_api = YOUR_API_KEY_HERE
   ```
3. Run `ping.py` to log a ping entry (schedule this to run periodically)
4. Run `currentplot.py` to view today's ping graph
5. Run `rename.py` at the end of each day to archive the log
6. Run `plot.py` to generate a compiled graph across all archived days

All paths are resolved automatically relative to the script locations — no manual path editing required.

#inprogress
