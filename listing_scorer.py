from listing_constructor import ListingConstructor

class Scorer(object):
    _defaults = [
        '_bedrooms', '_bathrooms', '_work_distance',
        '_lot_size', '_raw_score', '_price_score',
        '_raw_price', '_data_set', '_passing_listing'

    ]
    _default_value = None

    def __init__(self, **kwargs):
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)

    def set_price_score(self, price):
        low = 250000.0
        high = 400000.0
        slope = -0.5/150000
        if self._raw_price < low:
            self._price_score = 1.0
        elif self._raw_price == high :
            self._price_score = 0.5
        else:
            self._price_score = (slope * self._raw_price) + 1.0

    def set_bedrooms(self):
        """"""
        self._bedrooms = 
    
    def set_data_set(self):
        self._data_set = ListingConstructor()

    def iter_data_set(self):
        for page in self._data_set:
            for listing in page:
                """"""

