import re
import json
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        
        '''print("Encountered a start tag:", tag)
        if tag == 'script' and attrs == [('data-zrr-key', 'static-search-page:search-app')]:
        '''

    def handle_endtag(self, tag):
        '''print("Encountered an end tag :", tag)'''

    def handle_data(self, data):
        '''print("Encountered some data  :", data)'''
        if "<!--{\"queryState\":{\"pagination\":{},\"usersSearchTerm\":" in data:
            self.desired_data = data
            desired_html_regex = re.compile("(?!<!--)\{[\s\S\n]*(?<=)}")
            clean_dict = re.search(desired_html_regex, self.desired_data).group(0)
            clean_actual_dict = json.loads(clean_dict)
            with open('output\\temp.json', 'w', encoding='utf-8') as g:
                json.dump(clean_actual_dict, g, ensure_ascii=False, indent=4)