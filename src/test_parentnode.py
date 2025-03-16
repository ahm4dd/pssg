import unittest


from parentnode import *

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_nochildren(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), '<div></div>')
    
    def test_to_html_with_props(self):
        parent_node = ParentNode("div", [], {"class":".container"})
        self.assertEqual(parent_node.to_html(), '<div class=".container"></div>')
    
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class":".container"})
        self.assertEqual(parent_node.to_html(), '<div class=".container"><span>child</span></div>')

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class":".container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class=".container"><span><b>grandchild</b></span></div>',
        )
    
    def test_eq(self):
        node = ParentNode("p", [])
        node2 = ParentNode("p", [])
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = ParentNode("p", [])
        node2 = ParentNode("a", [])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = ParentNode("p", [])
        self.assertEqual(node.__repr__(), "ParentNode(p, [], None)")
