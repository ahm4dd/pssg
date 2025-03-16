from htmlnode import *
from leafnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == "":
            raise ValueError("No tag was provided for the ParentNode")
        if self.value == "":
            raise ValueError("No value was provided for the ParentNode")
        
        result = f"<{self.tag}>"
        for child in self.children:
            if isinstance(child, LeafNode):
                result = result + child.to_html()
            if isinstance(child, ParentNode):
                result = result + child.to_html()

        return f"{result}</{self.tag}>"    