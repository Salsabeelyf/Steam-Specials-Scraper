from selectolax.parser import HTMLParser
from selectolax.parser import Node
from config.tools import get_config
import helpers.network as n
import helpers.parse as p
import helpers.extract as ex


config = {}

def load_config(load_from_file= False):
    global config
    config = get_config(load_from_file)

# Get games div elements, extract exch game info and save to a list of Game objects
# return games
def get_games_as_list():
    html = n.extract_html(url= config.get('url'),
                                timeout= config.get('timeout'),
                                wait_for_selector= config.get('container').get('selector'),
                                scroll_to_selector= config.get('game_item').get('selector'))
    
    games_elements = find_games_elements(html)
    print('Extracting games info .....')
    games = [extract_game_info(game) for game in games_elements]
    return games


# Find games divs nodes
def find_games_elements(html):
    tree = HTMLParser(html)
    games = tree.css(config.get('game_item').get('selector'))
    
    return games# Export info into output csv file


# Extract info from each game div element
def extract_game_info(game: Node):
    raw_attrs = p.get_raw_attributes(game, config.get('attribute_item'))
    game_obj =  ex.process_attributes(raw_attrs)
    return game_obj