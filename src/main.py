from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
    #testNode = TextNode("This is some anchor text", TextType.LINK)
    #print(testNode.__repr__())

    #testHTMLNode = HTMLNode("a", "link", None, props={"href":"www.google.com", "hello":"test"})
    #print(testHTMLNode.props_to_html())

    #testLeafNode = LeafNode("p", "This is a paragraph of text.")
    #print(testLeafNode.to_html())

    #testLeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
    #print(testLeafNode2.to_html())
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    print(node.to_html())

main()