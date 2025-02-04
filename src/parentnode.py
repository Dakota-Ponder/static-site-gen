from htmlnode import *

# class that handles the nesting of HTML nodes inside of one another
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if not self.children:
            raise ValueError("Parent node must have a child")
        else:
            props_str = self.props_to_html()
            inner_html = ""
            for child in self.children:
                inner_html += child.to_html()
                
            return f"<{self.tag}{props_str}>{inner_html}<{self.tag}/>"