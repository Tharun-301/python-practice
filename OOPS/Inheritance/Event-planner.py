# The goal of this program is to build a simple Event Planner (calendar-like system) using Python.
import datetime as dt


class EventPlanner:

    def __init__(self, year):
        self.year = year
        self.events = {}

    def add_event(self, when, details):


        if when.date() < dt.date.today() or when.year != dt.date.today().year:
            raise Exception("Invalid Date")

        self.events[when] = details

    def remove_event(self, when):
        if when in self.events:
            del self.events[when]

    def list_events(self):

        print(f"\nEvents for {self.year}:\n")

        for event_time, details in self.events.items():

            formatted_time = event_time.strftime("%d %B, %A %Y, %I:%M %p")

            print(formatted_time)
            print("Details:", details)
            print()



year = int(input("Enter Year: "))

planner = EventPlanner(year)

for i in range(3):

    date_input = input("Enter Date (dd/mm/yyyy): ")
    day, month, year = map(int, date_input.split('/'))

    time_input = input("Enter Time (hh:mm): ")
    hour, minute = map(int, time_input.split(':'))

    when = dt.datetime(year, month, day, hour, minute)

    details = input("Details of Event: ")

    planner.add_event(when, details)


planner.list_events()