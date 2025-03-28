import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)

def extract_title(markdown):
    lines = markdown.split('\n')

    for line in lines:
        if re.search(r'^#{1}\s(.*?)+$', line.strip()) is not None:
             return line.split('# ', 1)[1].strip()
    
    raise Exception('h1 not found')

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