import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_eq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Hello, world!")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")