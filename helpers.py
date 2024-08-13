from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from tabulate import tabulate
import pandas as pd
import constants as c
from classes import Game

def get_games_as_list(url):
    html = extract_html(url)
    games_elements = find_games_elements(html)
    games = [extract_game_info(game) for game in games_elements]
    return games

def extract_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state('networkidle', timeout = c.TIMEOUT)
        page.wait_for_selector('div.sale_item_browser', timeout= c.TIMEOUT)
        
        scroll_to_element(page, c.game_div_locator)
        
        return page.inner_html('body')

def scroll_to_element(page, element_locator):
    while(not page.is_visible(element_locator)):
        page.mouse.wheel(0,500)


def find_games_elements(html):
    tree = HTMLParser(html)
    games = tree.css(c.game_div_locator)
    
    return games


def extract_game_info(game):
    title = game.css_first(c.title_div_locator).text()
    link_to_thumbnail = game.css_first(c.link_to_thumbnail_locator.format(title)).attrs['src']
    tags = [tag.text() for tag in game.css(c.category_tags_locator)[:5]]
    
    rating, no_of_reviews = get_rating_info(game)

    original_price, discounted_price, discount_percent = get_price_info(game)

    return  Game(title,
                 link_to_thumbnail,
                 tags,
                 rating,
                 no_of_reviews,
                 original_price,
                 discounted_price,
                 discount_percent)

def get_price_info(game):
    price_info_div = game.css_first(c.price_info_locator)
    if(price_info_div.attrs['class'].index('Discounted')):
        prices = game.css(f'{c.price_info_locator} > div > div')
        original_price = prices[0].text()
        discounted_price = prices[1].text()
        discount_percent = price_info_div.child.text()

    else:
        original_price, discounted_price, discount_percent
    
    return original_price, discounted_price, discount_percent

def get_rating_info(game):
    rating_info = game.css_first(c.rating_locator).text().split('|')
    rating = rating_info[0]
    rating_info[1] = rating_info[1].replace(' ', '')
    no_of_reviews = rating_info[1][:rating_info[1].index('U')]

    return rating, no_of_reviews
    
def export_to_csv(games):
    df = pd.DataFrame(games)
    df.to_csv(c.file_name, index=False)