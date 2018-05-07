#! python3
# pyuseful.py - Useful functions.

import datetime


def is_working_day(date, holidays=None):
    """Checks whether a date is a working date."""
    holidays = holidays if holidays is not None else list()

    if date.weekday() > 4 or date in holidays:
        return False

    return True


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


def working_days_between(from_date, to_date, holidays_list=None):
    """Returns the number of working days between two dates."""
    days = 0
    tmp_date = from_date + datetime.timedelta(days=1)

    while tmp_date <= to_date:
        if is_working_day(tmp_date, holidays_list):
            days += 1

        tmp_date = tmp_date + datetime.timedelta(days=1)

    return days
