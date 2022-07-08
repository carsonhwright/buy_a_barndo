from pathlib import Path
import os, json

from zillow_html_parser import MyHTMLParser

IMPORTANT_SCALE_FACTORS = {'bed': 4, 'lot_size': 3, 'raw_dist': 2, 'bath': 1}

class ListingConstructor():
    _defaults = [
        '_raw_dict',    '_bedrooms',       '_baths',
        '_lot_size',    '_raw_dist',       '_raw_scale',
        '_raw_html',    '_full_page_list', '_county_dictionaries'
    ]
    _default_value = None

    def __init__(self, **kwargs):
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)
        self.set_county_dictionaries()
    
    def set_raw_html(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self._raw_html = f.read()

    def set_full_page_list(self):
        parser = MyHTMLParser()
        parser.feed(self._raw_html)
        with open('output\\temp.json', 'r') as f:
            temp = json.load(f)
        self._full_page_list = temp["cat1"]["searchResults"]["listResults"]
    
    def set_county_dictionaries(self):
        paths = []
        self._county_dictionaries = {}
        for files in os.listdir(".\\output\\"):
            if files.endswith('.html'):
                paths.append(Path(f'.\\output\\{files}'))
        for path in paths:
            self.set_raw_html(path)
            self.set_full_page_list()
            self._county_dictionaries[path.stem] = self._full_page_list
        