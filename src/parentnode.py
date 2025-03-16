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
        
        result = f""
        if self.props is None or self.props == {}:
            result = f'<{self.tag}>' 
        else:
            result = f'<{self.tag} {self.props_to_html()}>'
            
        for child in self.children:
            if isinstance(child, LeafNode):
                result = result + child.to_html()
            if isinstance(child, ParentNode):
                result = result + child.to_html()

        return f"{result}</{self.tag}>"   

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def __eq__(self, parentNode):
        return self.tag == parentNode.tag and self.children == parentNode.children and self.props == parentNode.props 