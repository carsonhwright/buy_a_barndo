import zillow_html_parser as zp

IMPORTANT_SCALE_FACTORS = {'bed': 4, 'lot_size': 3, 'raw_dist': 2, 'bath': 1}

def ListingConstructor(object):
    _defaults = [
        '_raw_dict', '_bedrooms', '_baths',
        '_lot_size', '_raw_dist', '_raw_scale'
    ]
    _default_value = None

    def __init__(self, **kwargs):
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)
    
    def __set_raw_dict__(self):
