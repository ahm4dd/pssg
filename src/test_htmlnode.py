import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","hello there",None, {"href":"www.google.com"})
        node2 = HTMLNode("a","hello there",None, {"href":"www.google.com"}) 
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = HTMLNode("a","hello there",None, {"href":"www.google.com"})
        node2 =  HTMLNode("p","hello there",None, {})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("a","hello there",["i"], {"href":"www.google.com"})
        self.assertEqual(node.__repr__(),f"HTMLNode(a, hello there, {node.children}, {node.props})")
    
    def test_props_to_html(self):
        node = HTMLNode("a","hello there",None, {"href":"www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="www.google.com"')