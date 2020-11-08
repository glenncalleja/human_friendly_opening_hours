from datetime import time, datetime
from human_friendly_opening_hours import (Opening, Weekdays)


def test_opening_hours_gen(shop_opening_hours, options):
    shop_opening_hours.add_opening(Opening(
        Weekdays.thu, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shop_opening_hours.opening_hours_description(options)))
    assert(res == 'Thur: 08:00 AM to 12:00 PM')
    shop_opening_hours.add_opening(Opening(
        Weekdays.fri, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shop_opening_hours.opening_hours_description(options)))
    assert(res == 'Thur, Fri: 08:00 AM to 12:00 PM')
    shop_opening_hours.add_opening(Opening(
        Weekdays.sat, time(9, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shop_opening_hours.opening_hours_description(options)))
    assert(res == 'Thur, Fri: 08:00 AM to 12:00 PM|Sat: 09:00 AM to 12:00 PM')
    shop_opening_hours.add_opening(Opening(
        Weekdays.wed, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shop_opening_hours.opening_hours_description(options)))
    assert(res == 'Wed - Fri: 08:00 AM to 12:00 PM|Sat: 09:00 AM to 12:00 PM')


def test_is_open(shop_opening_hours):
    shop_opening_hours.add_opening(Opening(
        Weekdays.thu, time(8, 0), time(12, 0)))
    assert(shop_opening_hours.is_open(datetime(2020, 11, 5, 10, 0, 0)) is True)
    assert(shop_opening_hours.is_open(datetime(2020, 11, 5, 19, 0, 0)) is False)
