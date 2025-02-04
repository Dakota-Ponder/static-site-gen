import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_leafnode_no_value_raises_error(self):
        node = LeafNode("p", None)
        self.assertEqual(node.value, None)
        
    def test_leafnode_no_tag(self):
        node = LeafNode(None, "This is a paragraph.")
        self.assertEqual(node.tag, None)
        
    def test_leafnode_no_children(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.children, None)
        
if __name__ == '__main__':
    unittest.main()