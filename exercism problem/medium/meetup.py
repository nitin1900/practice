#solution... copy-pasted from site changed from ai all same logics

from calendar import day_name, monthrange, weekday
from datetime import date


class MeetupDayException(Exception):
    pass


START_DAY = {
    'first': 1,
    'second': 8,
    'third': 15,
    'fourth': 22,
    'fifth': 29,
    'teenth': 13,
    'last': None
}


def meetup(year, month, which, week_day):
    if which not in START_DAY:
        raise MeetupDayException(f'What is "{which}"?')

    if week_day not in day_name:
        raise MeetupDayException(f'Unknown day: "{week_day}"')

    start_day = START_DAY[which] or monthrange(year, month)[1] - 6

    try:
        start_day_wday = weekday(year, month, start_day)
        wanted_wday = list(day_name).index(week_day)

        delta = (wanted_wday - start_day_wday) % 7

        return date(year, month, start_day + delta)

    except ValueError:
        raise MeetupDayException("That day does not exist.")


# ---------------- INTERACTIVE PART ----------------#only changed by ai this part...

print("=== Meetup Day Finder ===")

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    print("\nWeek options:")
    print("first, second, third, fourth, fifth, teenth, last")
    which = input("Enter week descriptor: ").lower()

    print("\nWeekday options:")
    print(", ".join(day_name))
    week_day = input("Enter weekday: ").capitalize()

    result = meetup(year, month, which, week_day)

    print(f"\nMeetup date: {result}")

except MeetupDayException as e:
    print(f"\nError: {e}")

except ValueError:
    print("\nInvalid input. Please enter numbers where required.")