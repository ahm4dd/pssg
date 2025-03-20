import unittest

from converter import *

class TestConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_type(self):
        node = TextNode("This is a text node", "Hello")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, url="www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props["href"], "www.google.com")

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, url="www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "www.google.com")
        self.assertEqual(html_node.props["alt"], "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(text_to_textnodes(text), [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
    
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        md = """
        This is **bolded** paragraph
        test test test

        - This is a list
        - with items

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\ntest test test",
                "- This is a list\n- with items",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type(self):
        markdown_block = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.HEADING)
        markdown_block = "This is a paragraph"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.PARAGRAPH)
        markdown_block = "```This is a code block```"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.CODING)
        markdown_block = "> This is a quote"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.QUOTE)
        markdown_block = "- This is an unordered list"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.UNORDERED_LIST)
        markdown_block = "1. This is an ordered list"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.ORDERED_LSIT)
        markdown_block = "1. This is an ordered list\n2. This is another ordered list"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.ORDERED_LSIT)

        markdown_block = "1. This is an ordered list\n3. This is another ordered list"
        with self.assertRaises(ValueError):
            block_to_block_type(markdown_block)
    
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_unordered_list(self):
        md = """
        - This is a list
        - with items
        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><ul><li>This is a list</li><li>with items</li></ul></div>",
        )
    def test_ordered_list(self):
        md = """
        1. This is a list
        2. with items
        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><ol><li>This is a list</li><li>with items</li></ol></div>",
        )

    def test_link(self):
        md = """
        This is a [link](https://boot.dev)
        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><p>This is a <a href=\"https://boot.dev\">link</a></p></div>",
        )
    def test_image(self):
        md = """
        This is a ![image](https://boot.dev)
        """

        html = markdown_to_html_node(md)
        self.assertEqual(
            html.to_html(),
            "<div><p>This is a <img src=\"https://boot.dev\" alt=\"image\"></img></p></div>",
        )