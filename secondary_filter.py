

class SecondaryFilter(object):
    """
    The purpose of this class is to further filter out listings based on more complex
    assessment criteria. 

    TODO Construct data set, word cloud constructor, garage checker
    """
    _defaults = [
        '_data_set', '_secondary_pass_listing'
    ]
    _volatiles = [
        '_bedrooms',    '_bathrooms',                   '_work_distance',
        '_lot_size',    '_raw_score',                   '_price_score',
        '_raw_price',   '_currently_assessed_listing',  '_raw_loc',
        '_bed_score',   '_bath_score',                  '_work_dist_score',
        '_lot_score'
    ]
    _default_value = None

    def __init__(self, **kwargs):
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(dict.fromkeys(self._volatiles, self._default_value))
        self.__dict__.update(kwargs)

    def set_data_set(self):
        """
        This should make an instance of the InitialListingScorer which is the first filter, and 
        set _data_set to InitialListingScorer._initial_pass_listing
        """