from io import StringIO
from html.parser import HTMLParser
import sys
import re

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()
        
    def handle_data(self, d):
        self.text.write(d)
        
    def get_data(self):
        return self.text.getvalue()
        
    def strip_tags(self, html):
        pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'
        html = re.sub(pattern, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

        pattern = r'<[ ]*style.*?\/[ ]*style[ ]*>' 
        html = re.sub(pattern, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

        pattern = r'<[ ]*meta.*?>'
        html = re.sub(pattern, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

        pattern = r'<[ ]*!--.*?--[ ]*>'
        html = re.sub(pattern, '', html, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
        
        self.feed(html)
        new_str = ""
        
        removal_list = ['\t']
        for s in removal_list:
            new_str = self.get_data().replace(s, '')
            
        return new_str
    