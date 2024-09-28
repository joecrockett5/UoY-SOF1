def display_dict(d: dict) -> None:
    """Prints a dictionary"""
    for key, value in d.items():
        print(f"{key} --> {value}")
    return


def concatenate_dicts(d1: dict, d2: dict) -> dict:
    """Concatenates two dictionaries"""
    d3 = dict()
    d3.update(d1)
    for key, value in d2.items():
        if key in d3:
            if type(d3[key]) == list:
                d3[key].append(value)
            else:
                d3[key] = [d3[key], value]
        else:
            d3[key] = value
    return d3


def map_list(keys: list, values: list) -> dict:
    """Maps a list of keys to a list of values"""
    if len(keys) != len(values):
        raise ValueError("The keys and values must be the same length")
    d = dict()
    for key, value in zip(keys, values):
        d[key] = value
    return d


def reverse_dict(d: dict) -> dict:
    """Reverses a dictionary"""
    d2 = dict()
    for key, value in d.items():
        d2[value] = key
    return d2
