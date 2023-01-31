import datetime


class Event:

    def __init__(self, title="", date=datetime.datetime.now()):
        self.title = title
        self.date = date

    def __repr__(self):
        return f"Event({self.date}, {self.title}"


events = [
    Event(title="Событие 1", date=datetime.datetime(2019, 4, 3)),
    Event(title="Событие 2", date=datetime.datetime(2022, 4, 3)),
    Event(title="Событие 3", date=datetime.datetime(2020, 4, 3)),
    Event(title="Событие 3", date=datetime.datetime(2018, 4, 3)),
]

events.sort(key=lambda event: event.date)

print(events)

