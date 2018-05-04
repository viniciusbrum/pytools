#! python3
# pyuseful.py - Useful functions.


def merge_list_dicts(list_dicts):
    """Merges a list of dictionaries overwriting duplicate keys from
    left to right."""
    new_dict = dict()

    for dictionary in list_dicts:
        new_dict = {**new_dict, **dictionary}

    return new_dict
