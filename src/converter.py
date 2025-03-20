import re
from htmlnode import *
from textnode import *
from leafnode import *
from parser import *
from enum import Enum
from parentnode import *

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
     elif re.findall(r'\d+. ', markdown_block) != []:
          max_number = float('-inf')
          for number in re.findall(r'\d+. ', markdown_block):
               if int(number.replace('. ','')) > max_number:
                    max_number = int(number.replace('. ',''))  

          for number in range(1, max_number):
               if number != int(re.findall(r'\d+. ', markdown_block)[number-1].replace('. ', '')):
                    raise ValueError('Line numbers are not in order.')
          return BlockType.ORDERED_LSIT
     else:
          return BlockType.PARAGRAPH
     
 
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            flattened_text = re.sub(r'\s*\n\s*', ' ', block)
            children.append(ParentNode("p", text_to_children(flattened_text)))
        
        elif block_type == BlockType.HEADING:
            heading_match = re.match(r'^(#{1,6}) (.+)$', block)
            if heading_match:
                level = len(heading_match.group(1))
                content = heading_match.group(2)
                children.append(ParentNode(f"h{level}", text_to_children(content)))
        
        elif block_type == BlockType.CODING:
            code_content = block[3:-3]
            if code_content.startswith('\n'):
                code_content = code_content[1:]
          
            text_node = TextNode(code_content, TextType.TEXT)
            code_html_node = text_node_to_html_node(text_node)
            children.append(ParentNode("pre", [ParentNode("code", [code_html_node])]))
        
        elif block_type == BlockType.QUOTE:
            quote_content = re.sub(r'^>\s?', '', block, flags=re.MULTILINE)
            quote_content = re.sub(r'\s*\n\s*', ' ', quote_content)
            children.append(ParentNode("blockquote", text_to_children(quote_content)))
        
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for item in block.split("- ")[1:]:
                if item.strip():
                    flattened_item = re.sub(r'\s*\n\s*', ' ', item.strip())
                    list_items.append(ParentNode("li", text_to_children(flattened_item)))
            children.append(ParentNode("ul", list_items))
        
        elif block_type == BlockType.ORDERED_LSIT:
            list_items = []
            items = re.split(r'\d+\.\s+', block)[1:]
            for item in items:
                if item.strip():
                    flattened_item = re.sub(r'\s*\n\s*', ' ', item.strip())
                    list_items.append(ParentNode("li", text_to_children(flattened_item)))
            children.append(ParentNode("ol", list_items))
    
    return ParentNode("div", children)
 
def text_to_children(text):
     html_nodes = []
     text_nodes = text_to_textnodes(text)
     for node in text_nodes:
          html_nodes.append(text_node_to_html_node(node))
     return html_nodes