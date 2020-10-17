Human Friendly Opening Hours - Display Opening Hours in a human-friendly way
========================================================================

*This is a work-in-progress package. Any contributions and suggestions, especially for a more Pythonic solution are welcome.*

**Human Friendly Opening Hours** is a Python 3 module which takes as input raw opening hours and allows you to display them in a human friendly way. 

```python
from human_friendly_opening_hours import OpeningHours, Opening, Weekdays, Options
from datetime import time, datetime

shopOpeningHours = OpeningHours()

shopOpeningHours.add_opening(Opening(Weekdays.thu, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.wed, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.tue, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.mon, time(8, 0), time(12, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.mon, time(15, 0), time(17, 0)))
shopOpeningHours.add_opening(Opening(Weekdays.fri, time(8, 0), time(14, 0)))

result = shopOpeningHours.opening_hours_description()

print('\n'.join(map(lambda x: str(x), result)))
```

The above will print the following string:
```
Monday: 08:00 to 12:00, 15:00 to 17:00
Tuesday - Thursday: 08:00 to 12:00
Friday: 08:00 to 14:00
```

You can also pass options to the opening_hours_description() as such:

```python
options = Options()
options.time_format = '%I:%M %p' # Show dates in 12hr format
options.days_of_the_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
result = shopOpeningHours.opening_hours_description(options)
````

The above will instead result in:
```
Mon: 08:00 AM to 12:00 PM, 03:00 PM to 05:00 PM
Tue - Thur: 08:00 AM to 12:00 PM
Fri: 08:00 AM to 02:00 PM
```

Additionally you can use 
```python
is_open = shopOpeningHours.is_open(datetime.now())
````
to check if the time passed matches the opening hours.