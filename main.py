import constants as c
import helpers as h
from classes import Game

def run():
    games = h.get_games_as_list(c.url)
    h.export_to_csv(games)

if __name__ == '__main__':
    run()
