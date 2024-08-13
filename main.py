from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import constants as c

def extract_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        TIMEOUT = 60000
        page.wait_for_load_state('networkidle', timeout = TIMEOUT)
        page.wait_for_selector('div.sale_item_browser', timeout= TIMEOUT)
        
        while(not page.is_visible(c.game_div_locator)):
              page.mouse.wheel(0,500)
        
        return page.inner_html('body')
    

def find_games(html):
    tree = HTMLParser(html)
    games = tree.css(c.game_div_locator)
    for game in games:
        title = game.css_first(c.title_div_locator).text()
        link_to_thumbnail = game.css_first(c.link_to_thumbnail_locator.format(title)).attrs['src']
        tags = [tag.text() for tag in game.css(c.category_tags_locator)[:5]]
        rating_info = game.css_first(c.rating_locator).text().split('|')
        rating = rating_info[0]
        rating_info[1] = rating_info[1].replace(' ', '')
        no_of_reviews = rating_info[1][:rating_info[1].index('U')]

        price_info_div = game.css_first(c.price_info_locator)
        if(price_info_div.attrs['class'].index('Discounted')):
            prices = game.css(f'{c.price_info_locator} > div > div')
            original_price = prices[0].text()
            discounted_price = prices[1].text()
            discount_percent = price_info_div.child.text()

        else:
            price = price_info_div.text()
    

if __name__ == '__main__':
    html = extract_html('https://store.steampowered.com/specials')
    find_games(html)