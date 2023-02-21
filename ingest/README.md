# Ingest
Collection of python scripts gathering data from multiples sources to predict game attendance in the NFL.

## Data souces
- NFL (games, teams, attendance): https://www.pro-football-reference.com/
- weather: darksky, tomorrow.io
- stadiums details: wikipedia
- population: https://github.com/cestastanford/historical-us-city-populations/tree/master/data

## Storage location
The code upload the ingested data on GCP Cloud Storage.
For it to work, you will need to specify your destination bucket and the path to your service account key (write permission in the destination bucket) in the config file.

## Recommended Update Frequency
- weather: daily
- game details: after the end of each game
- games schedule: before the start of a new season, and after the end of each playoff game
- stadiums: yearly
- population: every 10 years