import json

config_file = 'config/config.json'

_config = {
    'timeout': 60000,
    'url': 'https://store.steampowered.com/specials',
    'csv_file': 'games_data.csv',
    'container':
        {
            'name': 'games_parent_div',
            'selector': 'div.sale_item_browser',
            'match': 'all',
            'type': 'node'
        },
    'game_item': {
            'name': 'game_div',
            'selector': 'div.sale_item_browser div.ImpressionTrackedElement',
            'match': 'all',
            'type': 'node'
        },
    'attribute_item': [
        {
            'name': 'title',
            'selector': 'div.StoreSaleWidgetTitle',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'thumbnail',
            'selector': 'div.CapsuleImageCtn img',
            'match': 'first',
            'type': 'src'
        },
        {
            'name': 'tags',
            'selector': 'a.WidgetTag',
            'match': 'all',
            'type': 'text'
        }
        ,{
            'name': 'rating',
            'selector': 'a.ReviewScore > div',
            'match': 'first',
            'type': 'text' # rating | no of reviews
        },
        {
            'name'"match": "first",
            "type": "text" 'no_of_reviews',
            'selector': 'a.ReviewScore > div',
            'match': 'first',
            'type': 'text' # rating | no of reviews
        },
        {
            'name': 'original_price',
            'selector': 'div.StoreSalePriceWidgetContainer',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'discounted_price',
            'selector': 'div.StoreSalePriceWidgetContainer',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'discount_percent',
            'selector': 'div.StoreSalePriceWidgetContainer',
            'match': 'first',
            'type': 'text'
        }
    ]
}


def get_config(load_from_file=False):
    if load_from_file:
        with open(config_file, 'r') as f:
            return json.load(f)
        
    return _config


def generate_config():
    with open(config_file, 'w') as f:
        json.dump(_config, f, indent=4)


if __name__ == '__main__':
    generate_config()