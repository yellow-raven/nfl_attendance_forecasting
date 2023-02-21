# get games schedule for a given year
# write data in a csv file
# store file in bucket/schedule/ folder
# schema
# year, week, date, time, game_details_url

def save_season_schedule(year):
    return "Please edit"

# get schedule from start year to end year
# run save_season_schedule(year) for each year in the interval

def save_schedule(start_year, end_year):
    years = list(range(start_year, end_year+1))
    for year in years:
        save_season_schedule(year)
    return "Job complete. {} season schedules saved.".format(len(years))