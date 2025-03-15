import functools

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self): 
        return functools.reduce(lambda acc, prop: acc + f'{prop}="{self.props[prop]}" ', self.props, "")