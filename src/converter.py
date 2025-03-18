from htmlnode import *
from textnode import *
from leafnode import *
from parser import *

def text_node_to_html_node(text_node):
       match text_node.text_type:
            case TextType.TEXT: 
                 return LeafNode(None, value=text_node.text)
            case TextType.BOLD:
                 return LeafNode('b', value=text_node.text) 
            case TextType.ITALIC:
                 return LeafNode('i', value=text_node.text)
            case TextType.CODE:
                 return LeafNode('code', value=text_node.text)
            case TextType.LINK:
                 return LeafNode('a', value=text_node.text, props={'href': text_node.url})
            case TextType.IMAGE:
                 return LeafNode('img', value='', props={'src': text_node.url, 'alt': text_node.text})
            case _:
                 raise Exception("TextNode type doesn't exist")

def text_to_textnodes(text): 
     result = []
     text_nodes = [TextNode(text, TextType.TEXT)]
     try:
          text_nodes = split_nodes_image(text_nodes)
          text_nodes = split_nodes_link(text_nodes)
          text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
          text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
          text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
     except Exception:
          pass
     return text_nodes