import constants as c
import helpers as h
from classes import Game

def run():
    # Get games as list from url
    games = h.get_games_as_list(c.url)

    # Export extracted data to output csv file
    h.export_to_csv(games)

if __name__ == '__main__':
    run()
