from classes import Game
import re


# Process raw attributes and get actual values needed, then create Game object
def process_attributes(attrs):
    
    transforms = {
        'tags': attrs.get('tags')[:5],  # tags --> get first 5 tags
        'rating': str.split(attrs.get('rating'), '|')[0], # rating --> split by | get first
        'no_of_reviews': ''.join(re.findall('\d+', str.split(attrs.get('no_of_reviews'), '|')[1])), # no_of_reviews --> split by | get second
        'discount_percent': str.split(str.replace(attrs.get('discount_percent'), 'New ', ''), ' ')[0], # discount_percent --> price --> get first
        'original_price': str.split(str.replace(attrs.get('original_price'), 'New ', ''), ' ')[1], # original_price --> price --> get second
        'discounted_price': str.split(str.replace(attrs.get('discounted_price'), 'New ', ''), ' ')[2] # discounted_price --> price --> get third
    }


    for k,v in transforms.items():
        if k in attrs:
            attrs[k] = v

    return attrs
