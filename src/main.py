from textnode import *
from htmlnode import * 
from leafnode import * 

def main():
    
    # p_node = LeafNode("p", "This is a paragraph of text.")
    node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    new_nodes = node.split_nodes_delimiter([node], "`", TextType.CODE)
    
    print(new_nodes)

    
main()