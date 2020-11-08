from human_friendly_opening_hours import OpeningHours, Options
import pytest


@pytest.fixture()
def shop_opening_hours():
    """
    Return a default opening hours
    """
    return OpeningHours()


@pytest.fixture(scope="module")
def options():
    """
    Return a default options
    """
    options = Options()
    options.time_format = '%I:%M %p'  # Show dates in 12hr format
    options.days_of_the_week = ["Mon", "Tue",
                                "Wed", "Thur", "Fri", "Sat", "Sun"]
    return options
