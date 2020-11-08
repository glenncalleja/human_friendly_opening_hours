from human_friendly_opening_hours import OpeningHours, Opening, Weekdays, Options
from datetime import time, datetime


def test_opening_hours_gen():
    shopOpeningHours = OpeningHours()
    options = Options()
    options.time_format = '%I:%M %p'  # Show dates in 12hr format
    options.days_of_the_week = ["Mon", "Tue",
                                "Wed", "Thur", "Fri", "Sat", "Sun"]
    shopOpeningHours.add_opening(Opening(
        Weekdays.thu, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shopOpeningHours.opening_hours_description(options)))
    assert(res == 'Thur: 08:00 AM to 12:00 PM')
    shopOpeningHours.add_opening(Opening(
        Weekdays.fri, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shopOpeningHours.opening_hours_description(options)))
    assert(res == 'Thur, Fri: 08:00 AM to 12:00 PM')
    shopOpeningHours.add_opening(Opening(
        Weekdays.sat, time(9, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shopOpeningHours.opening_hours_description(options)))
    assert(res == 'Thur, Fri: 08:00 AM to 12:00 PM|Sat: 09:00 AM to 12:00 PM')
    shopOpeningHours.add_opening(Opening(
        Weekdays.wed, time(8, 0), time(12, 0)))
    res = '|'.join(
        map(lambda x: str(x), shopOpeningHours.opening_hours_description(options)))
    assert(res == 'Wed - Fri: 08:00 AM to 12:00 PM|Sat: 09:00 AM to 12:00 PM')


def test_is_open():
    shopOpeningHours = OpeningHours()
    shopOpeningHours.add_opening(Opening(
        Weekdays.thu, time(8, 0), time(12, 0)))
    assert(shopOpeningHours.is_open(datetime(2020, 11, 5, 10, 0, 0)) is True)
    assert(shopOpeningHours.is_open(datetime(2020, 11, 5, 19, 0, 0)) is False)

