url = 'https://store.steampowered.com/specials'
file_name = 'games_data.csv'
TIMEOUT = 60000
game_div_locator = "div.sale_item_browser div.ImpressionTrackedElement"
title_div_locator = 'div.StoreSaleWidgetTitle'
link_to_thumbnail_locator = 'img[alt="{0}"]'
category_tags_locator = 'a.WidgetTag'
rating_locator = 'a.ReviewScore > div' # rating | no of reviews
price_info_locator = 'div.StoreSalePriceWidgetContainer'