from io import StringIO
from html.parser import HTMLParser
import sys

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
        self.feed(html)
        new_str = ""
        
        removal_list = ['\t']
        for s in removal_list:
            new_str = self.get_data().replace(s, '')
            
        return new_str
    