from textnode import *
from htmlnode import * 

def main():
    
        # Create an HTMLNode with some properties
    node = HTMLNode(tag="a", value="Click here", children=[1], props={"href": "https://example.com"})

    # Print the representation of the node
    print(repr(node))

    
main()