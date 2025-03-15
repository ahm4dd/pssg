from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url

    def __eq__(self, textNode):
        return self.text == textNode.text and self.text_type == textNode.text_type and self.url == textNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

