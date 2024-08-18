from typing import Type
from selectolax.parser import Node
from selectolax.parser import HTMLParser

# use attribute config to get raw attributes from Node
def get_raw_attributes(node: Node | str, items: list):
    if not issubclass(Node, type(node)):
         node = HTMLParser(node)

    parsed = {}

    for item in items:
        name = item.get('name')
        selector = item.get('selector')
        match = item.get('match')
        match_type = item.get('type')

        if match == 'first':
            element = node.css_first(selector)
            if match_type == 'node':
                parsed[name] = element
            elif match_type == 'text':
                parsed[name] = element.text(separator=' ')
            elif match_type == 'src':
                parsed[name] = element.attrs['src']

        if match == 'all':
            elements = node.css(selector)
            if match_type == 'node':
                parsed[name] = elements
            elif match_type == 'text':
                parsed[name] = [e.text() for e in elements]
            elif match_type == 'src':
                parsed[name] = [element.attrs['src'] for e in elements]


    return parsed