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

def split_nodes_image(old_nodes):
    result = []

    for node in old_nodes:
        if node.text == "":
            continue

        if not extract_markdown_images(node.text):
            result.append(node)
            continue

        temp_result = []
        remaining_text = node.text

        for image in extract_markdown_images(remaining_text):
            image_alt = image[0]
            image_link = image[1]
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            before_text = sections[0]
            remaining_text = sections[1]
            if before_text:
                temp_result.append(TextNode(before_text, TextType.TEXT))
            temp_result.append(TextNode(image_alt, TextType.IMAGE, url=image_link))

        if remaining_text:
            temp_result.append(TextNode(remaining_text, TextType.TEXT))

        result.extend(split_nodes_image(temp_result))

    return result

def split_nodes_link(old_nodes):
    result = []

    for node in old_nodes:
        if node.text == "":
            continue

        if not extract_markdown_links(node.text):
            result.append(node)
            continue

        temp_result = []
        remaining_text = node.text

        for link in extract_markdown_links(remaining_text):
            link_text = link[0]
            link_url = link[1]
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            before_text = sections[0]
            remaining_text = sections[1]
            if before_text:
                temp_result.append(TextNode(before_text, TextType.TEXT))
            temp_result.append(TextNode(link_text, TextType.LINK, url=link_url))

        if remaining_text:
            temp_result.append(TextNode(remaining_text, TextType.TEXT))

        result.extend(split_nodes_link(temp_result))

    return result