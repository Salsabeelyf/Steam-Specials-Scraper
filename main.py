from helpers import helpers as h, output as o
from config.tools import get_config

def run():

    # Load configurations from json file
    h.load_config(True)

    # Get games as list from url
    games = h.get_games_as_list()

    # Export extracted data to output csv file
    o.export_to_csv(games, get_config().get('csv_file'))

if __name__ == '__main__':
    run()
