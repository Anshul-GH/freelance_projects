# this will hold the parameters that can be modified, if needed

config = {
    "MIN_K": 4,
    "MAX_K": 9
}


# method to expose the parameters
def get_config(param, default=None):
    cv = config.get(param)
    return cv