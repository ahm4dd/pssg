import re
from htmlnode import *
from textnode import *
from leafnode import *
from parser import *
from enum import Enum

class BlockType(Enum):
     PARAGRAPH = 'paragraph'
     HEADING = 'heading'
     CODING = 'code'
     QUOTE = 'quote'
     UNORDERED_LIST = 'unordered_list'
     ORDERED_LSIT = 'ordered_list'



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

def markdown_to_blocks(markdown):
    result_blocks = []
    temp_blocks = []
    blocks = markdown.split("\n\n")
    
    for block in blocks:
        if block.strip() == "":
            continue
        temp_blocks.extend(block.strip().split('    \n    '))
    for block in temp_blocks:
        result_blocks.append(block.strip('\n    ').replace('    ', ''))
    
    return result_blocks


def block_to_block_type(markdown_block):

     if re.match(r'^#{1,6} ', markdown_block) is not None:
          return BlockType.HEADING 
     elif markdown_block.startswith('```') and markdown_block.endswith('```'):
          return BlockType.CODING
     elif markdown_block.startswith('>'):
          return BlockType.QUOTE
     elif markdown_block.startswith('- '):
          return BlockType.UNORDERED_LIST
     #TODO
     # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
     # If none of the above conditions are met, the block is a normal paragraph.
     """
     elif re.match(r'^[1-9]. ', markdown_block) is not None:
          return BlockType.ORDERED_LSIT
     """