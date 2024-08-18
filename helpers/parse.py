from selectolax.parser import Node

# use attribute config to get raw attributes from Node
def get_raw_attributes(node: Node, items: list):
    parsed = {}

    for item in items:
        name = item.get('name')
        selector = item.get('selector')
        match = item.get('match')
        type = item.get('type')

        if match == 'first':
            element = node.css_first(selector)
            if type == 'text':
                parsed[name] = element.text(separator=' ')
            elif type == 'src':
                parsed[name] = element.attrs['src']

        if match == 'all':
            elements = node.css(selector)
            if type == 'text':
                parsed[name] = [e.text() for e in elements]
            elif type == 'src':
                parsed[name] = [element.attrs['src'] for e in elements]

    return parsed