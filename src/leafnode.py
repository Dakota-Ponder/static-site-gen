from htmlnode import *

# leaf node class that is a child of htmlnode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        
        super().__init__(tag, value, None, props)
        self.children = None
        
    # renders a leaf node as an HTML string (by returning a string).
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value 
        props_str = self.props_to_html() 
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"