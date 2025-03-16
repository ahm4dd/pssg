import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for text_node in old_nodes:
        if text_node.text_type != TextType.TEXT:
            result.extend(text_node)
        if delimiter not in text_node.text:
            raise ValueError(f"The delimiter {delimiter} was not found in the following text: {text_node.text}")
        
        temp_result = []
        text_splitted = text_node.text.split(delimiter)
        temp_result.append(TextNode(text_splitted[0], TextType.TEXT))
        match text_type, delimiter:
            case TextType.BOLD, "**":
                temp_result.append(TextNode(text_splitted[1], TextType.BOLD))
            case TextType.ITALIC, "_":
                temp_result.append(TextNode(text_splitted[1], TextType.ITALIC))
            case TextType.CODE, "`":
                temp_result.append(TextNode(text_splitted[1], TextType.CODE))
            case _:
                raise Exception("TextNode type doesn't exist")
            
        temp_result.append(TextNode(text_splitted[2], TextType.TEXT))
        result.extend(temp_result)

    return result


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)