from enum import Enum 
from leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold" 
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url 
        
    def text_node_to_html_node(text_node):
        """Converts a TextNode to an HTMLNode."""
        # if text_node enum type is none of the types then raise exception
        if text_node.text_type not in TextType:
            raise Exception("Invalid text type")
        if text_node.text_type == TextType.NORMAL:
            # return a leaf node with no tag, just text 
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode("bold", text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode("italic", text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text)
        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
        
    # checks if the two TextNode objects are equal 
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False 
        return (
            self.text == other.text and
            self.text_type == other.text_type and 
            self.url == other.url
        ) 
        
        
    # returns string representation of the TextNode 
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})" 