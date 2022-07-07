import re
import json
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        
        '''print("Encountered a start tag:", tag)
        if tag == 'script' and attrs == [('data-zrr-key', 'static-search-page:search-app')]:
            breakpoint()'''

    def handle_endtag(self, tag):
        '''print("Encountered an end tag :", tag)'''

    def handle_data(self, data):
        '''print("Encountered some data  :", data)'''
        if "<!--{\"queryState\":{\"pagination\":{},\"usersSearchTerm\":" in data:
            self.desired_data = data
            # print(data)

    def handle_scraper_output(self, data):
        """
        
        """
        parser = MyHTMLParser()
        with open('output/Fulton County.html', 'r', encoding='utf-8') as f:
            html_feed = f.read()

        parser.feed(html_feed)
        desired_html_regex = re.compile("(?!<!--)\{[\s\S\n]*(?<=)}")
        clean_dict = re.search(desired_html_regex, parser.desired_data).group(0)
        clean_actual_dict = json.loads(clean_dict)

        # individual houses are clean_actual_dict["cat1"]["searchResults"]["listResults"][list_index]
        # at this point I can parse desired html data from each house, now I need to implement
        for unit_index in range(len(clean_actual_dict["cat1"]["searchResults"]["listResults"])):
            print(clean_actual_dict["cat1"]["searchResults"]["listResults"][unit_index]["price"])