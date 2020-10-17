from human_friendly_opening_hours import OpeningHours, Opening, Weekdays, Options
from datetime import time, datetime

shopOpeningHours = OpeningHours()

options = Options()
options.time_format = '%I:%M %p'

shopOpeningHours.add_opening(Opening(Weekdays.thu, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.wed, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.tue, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.mon, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.mon, time(15, 0), time(17, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.fri, time(8, 0), time(14, 0)))

result = shopOpeningHours.opening_hours_description()

print('\nManually print the result from FriendlyOpeningHour List')
for i in result:
    print(i.weekdays, ': ', i.time)

print('\nPrint all as string in one line')
print('\n'.join(map(lambda x: str(x), result)))

print('\nCheck if Currently Open')
print(shopOpeningHours.is_open(datetime.now()))
