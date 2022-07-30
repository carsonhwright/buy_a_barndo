from listing_constructor import ListingConstructor

MIN_LOT_SIZE, IDEAL_LOT_SIZE = 0.25, 0.5
CARSON_WORK_LOC_LAT, CARSON_WORK_LOC_LONG = 33.787034278680466, -84.37958931718705
ANGELA_WORK_LOC_LAT, ANGELA_WORK_LOC_LONG = 33.80001232871316, -84.3243549597764
MIN_SCORE = 6.0
ACRE_TO_SQFT = 43560.0
class ListingScorer(object):
    _defaults = [
        '_data_set', '_initial_pass_listing', '_min_score'
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
        self.set_data_set()
        self.score_data_set()

    def clear_volatiles(self):
        self.__dict__.update(dict.fromkeys(self._volatiles, self._default_value))

    def set_price_score(self):
        low = 250000.0
        high = 400000.0
        slope = -0.5/150000

        if self._raw_price < low:
            self._price_score = 1.0
        elif self._raw_price == high :
            self._price_score = 0.5
        else:
            self._price_score = (slope * self._raw_price) + 1.833333
    
    def set_bed_score(self):
        if self._bedrooms >= 4:
            self._bed_score = 4.0
        elif self._bedrooms == 3:
            self._bed_score = 3.0
        elif self._bedrooms == 2:
            self._bed_score = 2.0
        elif self._bedrooms < 2:
            self._bed_score = 1.0
    
    def set_bath_score(self):
        if self._bathrooms >= 3:
            self._bath_score = 3.0
        elif self._bathrooms < 3 and self._bathrooms >= 2.5:
            self._bath_score = 2.5
        elif self._bathrooms < 2.5 and self._bathrooms >= 2:
            self._bath_score = 2.0
        elif self._bathrooms < 2:
            self._bath_score = 1.0

    def set_lot_score(self):
        if self._lot_size >= IDEAL_LOT_SIZE:
            self._lot_score = 1.0
        elif self._lot_size >= MIN_LOT_SIZE and self._lot_size < IDEAL_LOT_SIZE:
            self._lot_score = 2 * self._lot_size
        else:
            self._lot_score = 0.5
    
    def set_raw_score(self):
        self._raw_score = (
            (self._bed_score + self._bath_score + self._lot_score)
            * self._price_score 
        )
    
    def set_data_set(self):
        """
        Parameters
        ----------
        self - Scorer obj

        this is intended to turn the large dictionary from listing_constructor called 
        _county_dictionaries and break it down into a list of dictionaries which contain the
        individual housing listings
        """
        self._data_set = []
        temp = ListingConstructor()
        pages = temp._county_dictionaries
        for page in pages:
            for listing in pages[page]:
                self._data_set.append(listing)


    def score_data_set(self):
        """
        This will iterate over the listings in _data_set and give them an initial scoring
        """
        self._initial_pass_listing = []
        for listing in self._data_set:
            self._currently_assessed_listing = listing
            self._raw_price = self._currently_assessed_listing["unformattedPrice"]
            self._bedrooms = self._currently_assessed_listing["beds"]
            self._bathrooms = self._currently_assessed_listing["baths"]
            self._raw_loc = self._currently_assessed_listing["latLong"]
            self._lot_size = self._currently_assessed_listing["hdpData"]["homeInfo"]["lotAreaValue"]
            if self._currently_assessed_listing["hdpData"]["homeInfo"]["lotAreaUnit"] == "sqft":
                self._lot_size = self._lot_size / ACRE_TO_SQFT
            self.set_price_score()
            self.set_bed_score()
            self.set_bath_score()
            self.set_lot_score()
            # all scores need to be set before this gets executed
            self.set_raw_score()
            temp = self._currently_assessed_listing["imgSrc"]
            # debugging output
            # print(f"bedscore: {self._bed_score} bathscore: {self._bath_score} lotscore: {self._lot_score} pricescore: {self._price_score}")
            # doing some debugging here
            
            if self._raw_score > MIN_SCORE:
                self._initial_pass_listing.append(self._currently_assessed_listing)
            self.clear_volatiles()
            