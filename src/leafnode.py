from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        #if self.value is None or self.value == "":
            #raise ValueError("All leaf nodes must have a value.")
        if self.tag is None or self.tag == "":
            return self.value
        if self.tag == "code":
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        if self.props is None or self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, leafnode):
        return self.tag == leafnode.tag and self.value == leafnode.value and self.props == leafnode.props
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"