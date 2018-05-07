#! python3
# pyuseful.py - Useful functions.


def merge_list_dicts(list_dicts):
    """Merges a list of dictionaries overwriting duplicate keys from
    left to right."""
    new_dict = dict()

    for dictionary in list_dicts:
        new_dict = {**new_dict, **dictionary}

    return new_dict


def sorted_dict(dictionary, by_keys=False, reverse=False):
    """Returns a sorted representation of a dictionary."""
    index = 0 if by_keys else 1
    return sorted(dictionary.items(), key=lambda item: item[index],
                  reverse=reverse)
