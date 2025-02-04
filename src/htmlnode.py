class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value 
        #               x if condition else y 
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError("The to_html method must be overridden by child classes.")
    
    def props_to_html(self):
        """
    Converts the props dictionary into a string of HTML attributes (non-Pythonic style).
    
    :return: A string representing HTML attributes, or an empty string if no props exist.
    """
        # check if empty 
        if self.props is None:
            return ""
        
        props_html = ""
        for key in self.props:
            value = self.props[key]
            props_html += f' {key}="{value}"'
            
        return props_html
    
    
    def __repr__(self):
        """
        Function that prints an HTMLNode object and see its tag, value, children, and props
        """
        props_str = self.props_to_html()
        children_count = len(self.children)
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={children_count}, props={props_str})"