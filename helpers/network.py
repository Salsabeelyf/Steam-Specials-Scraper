from playwright.sync_api import sync_playwright
from playwright.sync_api import Page


# Open url and wait till fully loaded
# return body
def extract_html(url, timeout, wait_for_selector, scroll_to_selector):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        print(f'{url} Loading .....')
        page.wait_for_load_state('networkidle', timeout = timeout)
        page.wait_for_selector(wait_for_selector, timeout= timeout)
        
        # scroll till games divs are visible
        scroll_to_element(page, scroll_to_selector)
        
        print(f'{url} Loaded Successfully')
        return page.inner_html('body')


# Scroll till element is visible
def scroll_to_element(page: Page, element_locator: str):
    while(not page.is_visible(element_locator)):
        page.mouse.wheel(0,500)