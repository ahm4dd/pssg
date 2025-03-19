from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from parser import *
from converter import *

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

    #node = TextNode(
    #"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #TextType.TEXT,
    #)
    #new_nodes = split_nodes_link([node])
    #print(new_nodes)
    
    #print(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
    #[
    #TextNode("This is ", TextType.TEXT),
    #TextNode("text", TextType.BOLD),
    #TextNode(" with an ", TextType.TEXT),
    #TextNode("italic", TextType.ITALIC),
    #TextNode(" word and a ", TextType.TEXT),
    #TextNode("code block", TextType.CODE),
    #TextNode(" and an ", TextType.TEXT),
    #TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    #TextNode(" and a ", TextType.TEXT),
    #TextNode("link", TextType.LINK, "https://boot.dev"),
    #]
   # print(markdown_to_blocks("""
   # This is **bolded** paragraph
   # 
   # This is another paragraph with _italic_ text and `code` here
   # This is the same paragraph on a new line
   # 
    #- This is a list
    #- with items
    #"""))
    print(block_to_block_type('1. hello \n2. hello\n3. hello'))
main()