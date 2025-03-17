from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from parser import *

def main():
    #testNode = TextNode("This is some anchor text", TextType.LINK)
    #print(testNode.__repr__())

    #testHTMLNode = HTMLNode("a", "link", None, props={"href":"www.google.com", "hello":"test"})
    #print(testHTMLNode.props_to_html())

    #testLeafNode = LeafNode("p", "This is a paragraph of text.")
    #print(testLeafNode.to_html())

    #testLeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
    #print(testLeafNode2.to_html())
    #node = ParentNode(
    #"p",
    #[
      #  LeafNode("b", "Bold text"),
      #  LeafNode(None, "Normal text"),
      #  LeafNode("i", "italic text"),
       # LeafNode(None, "Normal text"),
    #],
    #)
    #print(node.to_html())
     
    #text = "Weird **text** to test"
    #text_splitted = text.split('**')
    #print(text_splitted)
    #nodes = split_nodes_delimiter([TextNode("Hello _test_ world", TextType.TEXT), TextNode("Hello test _world_", TextType.TEXT)], "_", TextType.ITALIC)

    #print(nodes)
    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))

    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text))

    #node = TextNode(
    #    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #    TextType.TEXT,
    #)
    #new_nodes = split_nodes_image([node])
    #print(new_nodes)

    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
main()