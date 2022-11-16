from datetime import datetime, timedelta, MAXYEAR, MINYEAR, date
from pprint import pprint

from event import Event, Workshop, Reminder
from helpers import generate_objects


class Calendar:
    def __init__(self, events=None):
        self._events = events or []

    @property
    def events(self):

        counter = 0
        for event in self._events:
            if datetime.now() < event.start_date <= datetime.now() + timedelta(weeks=4):
                counter += 1

        return f'for incoming 4 weeks, you have {counter} events'

    @events.setter
    def events(self, value):

        if not isinstance(value, (Event, Workshop, Reminder)):
            raise TypeError(f'Wrong data type: {type(value)}')

        self._events.append(value)

    def filter_by_data(self, start_date=datetime.min, end_date=datetime.max):

        events = []

        for event in self._events:
            if start_date <= event.start_date < end_date:
                events.append(event)

        return events

    def filter_by_duration(self, duration=0, duration_min=0, duration_max=None):

        if duration is not None:
            duration_min = duration_max = duration

        events = []

        for event in self._events:
            if event.duration in range(duration_min,
                                       (duration_max + 1 if duration_max is not None else event.duration + 1)):
                events.append(event)

        return events

    def __len__(self):
        return len(self._events)


data = generate_objects()

c = Calendar(data)

# f = c.filter_by_data(datetime.now(), datetime.now() + timedelta(weeks=4))
f = c.filter_by_duration(duration_min=200)
print(f)
pprint(c)
# pprint(c.events)
# print(len(c))
