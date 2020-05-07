import os

config = {
    "TOP_N": 1000,
    "BASE_URL": "https://www.imdb.com/search/title/?",
    "RELEASE_DATE": "release_date=2019-01-01,2020-12-31",
    "SORT_ON": "sort=num_votes,desc",
    "COUNT": 250,
    "START": 1,
    "REF_": "ref_=adv_next"
}

# method to expose the configuration variables
def get_config(param, default=None):
    cv = config.get(param)
    return cv 