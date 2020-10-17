from enum import IntEnum
from itertools import groupby
from operator import itemgetter
Weekdays = IntEnum('Weekdays', 'mon tue wed thu fri sat sun', start=0)


class Options:
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    time_format = '%H:%M'


class Opening:
    def __init__(self, weekday, opening_time, closing_time):
        self.weekday = weekday
        self.opening_time = opening_time
        self.closing_time = closing_time


class HumanFriendlyOpeningHour:
    def __init__(self, weekdays, time):
        self.weekdays = weekdays
        self.time = time

    def __str__(self):
        return self.weekdays + ": " + self.time


class OpeningHours:
    opening_hours = []

    def __init__(self):
        pass

    def __grouped_week_days(self, weekdays, options):
        """
        Takes a list of weekdays, and returns them grouped in a friendly
        string. For example:
        Mon, Tue, Wed, Fri, Sat returns 'Mon - Wed, Fri, Sat'
        """
        weekdays = list(map(lambda a: a, weekdays))
        res = []
        for k, g in groupby(enumerate(weekdays), lambda i_x: i_x[0] - i_x[1]):
            res.append(list(map(itemgetter(1), g)))
        final_res = []
        str_res = ''
        for day_list in res:
            if len(day_list) == 1:
                str_res = options.days_of_the_week[day_list[0].value]
            elif len(day_list) == 2:
                str_res = options.days_of_the_week[day_list[0].value] + ', ' + options.days_of_the_week[day_list[-1].value]
            else:
                str_res = options.days_of_the_week[day_list[0].value] + ' - ' + options.days_of_the_week[day_list[-1].value]
            final_res.append(str_res)
        return ', '.join(final_res)

    def opening_hours_description(self, options = Options()):
        """
        Returns the opening hours in a friendly format
        """
        weekday_dict = self.__weekday_dict(options)
        new_dict = {}
        for k, v in weekday_dict.items():
            new_dict.setdefault(v, []).append(k)
        res_dict = {self.__grouped_week_days(v, options): k for k, v in new_dict.items()}
        human_friendly_opening_hours_list = []
        for key, value in res_dict.items():
            human_friendly_opening_hours_list.append(HumanFriendlyOpeningHour(key, value))
        return human_friendly_opening_hours_list

    def __weekday_dict(self, options):
        """
        Takes opening hours list and returns with the values being a condensed
        opening hour description e.g. 13:00 - 16:00 and the keys being all days
        of the week which match this opening hour description
        """
        weekday_set = list(set(map(lambda a: a.weekday, self.opening_hours)))
        weekday_dict = {}
        for weekday in weekday_set:
            matching_opening_hours = filter(lambda x: x.weekday == weekday,
                                            self.opening_hours)
            weekday_list = map(lambda x: x.opening_time.strftime(options.time_format) +
                               ' to ' + x.closing_time.strftime(options.time_format),
                               matching_opening_hours)
            weekday_dict[weekday] = ', '.join(weekday_list)
        return weekday_dict

    def add_opening(self, opening):
        """
        Add an opening to the OpeningHours instance
        """
        self.opening_hours.append(opening)

    def is_open(self, datetime):
        """
        Checks if the OpeningHours instance is open at the passed time
        """
        for openingHour in self.opening_hours:
            if (openingHour.weekday.value == datetime.weekday() and
                    (openingHour.opening_time <= datetime.time()
                     <= openingHour.closing_time)):
                return True
        return False

