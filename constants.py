# URL to steam specials
url = 'https://store.steampowered.com/specials'

# Output file name
file_name = 'games_data.csv'

# Timeout value for playwright
TIMEOUT = 60000

# Locators
game_div_locator = "div.sale_item_browser div.ImpressionTrackedElement"
title_div_locator = 'div.StoreSaleWidgetTitle'
link_to_thumbnail_locator = 'img[alt="{0}"]'
category_tags_locator = 'a.WidgetTag'
rating_locator = 'a.ReviewScore > div' # rating | no of reviews
price_info_locator = 'div.StoreSalePriceWidgetContainer' # price parent div locator