from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == "":
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"