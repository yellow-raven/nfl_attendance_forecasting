# to had random sleep time to be nice to their server and mimic human behaviors
from random import randint
from time import sleep
import requests

# get game details
# do not forget to add a user agent (Mozilla/5.0) to requests
# write data into a csv file
# upload csv file to cloud storage

def save_game_details(url):
    delay = randint(5,15)
    sleep(delay)
    return "Please edit"

# get_games_url(schedules_folder)

# get games details over a list of game urls

def save_games_details(urls):
    for url in urls:
        save_game_details(url)
    return "Job complete. {} game details saved.".format(len(urls))