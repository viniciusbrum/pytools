#! python3
# pyuseful.py - Useful functions.

import datetime


def _permutations(tail, perms, head=''):
    if len(tail) == 1:
        perms.append(head + tail)
        return

    for token in tail:
        token_tail = tail.replace(token, '')
        _permutations(token_tail, perms, head + token)


def get_permutations(string):
    """Returns permutations for a string."""
    permutations = list()
    _permutations(string, permutations)
    return permutations


def greatest_common_divisor(x, y):
    """Return the greatest common divisor of x and y."""
    if x == 0:
        return y

    if y == 0:
        return x

    if x == y:
        return x

    if x < y:
        lower = x
        remainder = y % x
    else:
        lower = y
        remainder = x % y

    return greatest_common_divisor(lower, remainder)


def is_working_day(date, holidays=None):
    """Checks whether a date is a working date."""
    if date.weekday() > 4 or (holidays and date in holidays):
        return False

    return True


def last_day_month(day):
    """Returns the last day of month."""
    day_next_month = day.replace(day=28) + datetime.timedelta(days=4)
    return day_next_month - datetime.timedelta(days=day_next_month.day)


def merge_list_dicts(list_dicts):
    """Merges a list of dictionaries overwriting duplicate keys from
    left to right."""
    new_dict = dict()

    for dictionary in list_dicts:
        new_dict = {**new_dict, **dictionary}

    return new_dict


def next_working_day(from_date, days=1, holidays_list=None):
    days = max(1, days)
    delta = datetime.timedelta(days=1)
    count = 0
    tmp_date = from_date

    if holidays_list:
        holidays_list = [holiday
                         for holiday in holidays_list
                         if (holiday > from_date and holiday.weekday() < 5)]

    while count < days:
        tmp_date += delta

        if is_working_day(tmp_date, holidays_list):
            count += 1

    return tmp_date


def previous_working_day(from_date, days=-1, holidays_list=None):
    days = min(-1, days)
    delta = datetime.timedelta(days=1)
    count = 0
    tmp_date = from_date

    if holidays_list:
        holidays_list = [holiday
                         for holiday in holidays_list
                         if (holiday < from_date and holiday.weekday() < 5)]

    while count > days:
        tmp_date -= delta

        if is_working_day(tmp_date, holidays_list):
            count -= 1

    return tmp_date


def sorted_dict(dictionary, by_keys=False, reverse=False):
    """Returns a sorted representation of a dictionary."""
    index = 0 if by_keys else 1
    return sorted(dictionary.items(), key=lambda item: item[index],
                  reverse=reverse)


def square_root(x, precision):
    s = 1
    e = x
    m = (s + e) / 2

    while e - s > precision:
        if m**2 > x:
            e = m
        else:
            s = m

        m = (s + e) / 2

    return m


def working_days_between(from_date, to_date, holidays_list=None):
    """Returns the number of working days between two dates."""
    working_days = 0
    holidays = 0
    delta = datetime.timedelta(days=1)
    tmp_date = from_date + delta

    if holidays_list:
        holidays = len([holiday
                        for holiday in holidays_list
                        if (tmp_date <= holiday <= to_date
                            and holiday.weekday() < 5)])

    while tmp_date <= to_date:
        if is_working_day(tmp_date):
            working_days += 1

        tmp_date += delta

    return working_days - holidays
