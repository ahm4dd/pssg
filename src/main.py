from textnode import *
from htmlnode import *

def main():
    testNode = TextNode("This is some anchor text", TextType.LINK)
    print(testNode.__repr__())

    testHTMLNode = HTMLNode("a", "link", None, props={"href":"www.google.com", "hello":"test"})
    print(testHTMLNode.props_to_html())
    
main()