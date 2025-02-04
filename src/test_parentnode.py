import unittest

from parentnode import *
from leafnode import * 

class TestParentNode(unittest.TestCase):
    def test_no_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("p", "This is a paragraph.")])
        self.assertEqual(node.tag, None)
        
    # test if there are no children 
    def test_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.children, [])
        
    