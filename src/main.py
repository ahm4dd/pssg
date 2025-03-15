from textnode import *

def main():
    testNode = TextNode("This is some anchor text", TextType.LINK)
    print(testNode.__repr__())

main()