from textnode import *
from htmlnode import * 
from leafnode import * 

def main():
    
    # p_node = LeafNode("p", "This is a paragraph of text.")
    a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    print(a_node.to_html())

    
main()