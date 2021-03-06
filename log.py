from entry import Entry

import re
import datetime


class Log:

    def __init__(self):
        self.entries = []

    # Creates a new entry in this log
    def new(self):
        name = input("What would you like to name this task? ")
        while True:
            try:
                minutes = input("How many minutes have you "
                                "spent working on it? ")
                minutesDelta = datetime.timedelta(minutes=int(minutes))
                break
            except ValueError:
                print("Invalid input. Please enter a number of minutes.")
        notes = []
        while True:
            noteText = input('Please enter notes for this task. '
                             'Enter "q" to finish. ')
            if noteText.upper() == "Q":
                break
            else:
                notes.append(noteText)
        self.entries.append(Entry(name, minutesDelta,
                            datetime.datetime.now(), notes))

    # Wrapper function to prompt user for lookup type
    def lookup(self):
        while True:
            option = input("Would you like to lookup by [d]ate, "
                           "[t]ime spent, [e]xact search, "
                           "or [p]attern match? ")

            if option.upper() == "D":
                self.find_by_date(datetime.datetime.now())
                break
            elif(option.upper() == "T"):
                while True:
                    phrase = input("How many minutes spent "
                                   "are you searching for? ")
                    try:
                        minutes = int(phrase)
                    except ValueError:
                        continue
                    break
                self.find_by_time_spent(minutes)
            elif option.upper() == "E":
                phrase = input("What phrase would you like to search for? ")
                self.find_by_exact_match(phrase)
                break
            elif option.upper() == "P":
                pattern = input("What regex would you like to search for? ")
                self.find_by_pattern(pattern)
                break
            else:
                print("Invalid option, please try again.")

    def find_by_date(self, date):
        # User set() to generate a unique,
        # sorted list of dates that have entries
        uniqueDates = list(set([entry.timestamp.date() for entry
                                in self.entries]))
        sortedDates = sorted(uniqueDates)

        # Print the list of dates and prompt for a selection
        for i, date in enumerate(sortedDates):
            print("{}: {}".format(i+1, date.strftime('%b %d, %Y')))

        while True:
            try:
                dateSelection = int(input("Select a date to "
                                          "view by number. "))
                if dateSelection in list(range(1, len(sortedDates)+1)):
                    break
                else:
                    print("That number isn't in the list of options. "
                          "Please try again.")
                    continue
            except ValueError:
                print('Not a valid input, please try again.')
                continue

        # Print all entries for the chosen date
        print("".join([str(entry) + '\n' for entry in self.entries
                      if entry.timestamp.date()
                      == sortedDates[dateSelection - 1]]))

    def find_by_time_spent(self, minutes):
        # Use a comprehension to grab all notes with the
        # given number of minutes
        matches = [entry for entry in self.entries
                   if entry.minutes == datetime.timedelta(minutes=minutes)]

        print("".join([str(entry) + '\n' for entry in matches]))

    def find_by_exact_match(self, phrase):
        # Use a comprehension to grab all entries containing the
        # given phrase in their title or note
        matches = [entry for entry in self.entries if phrase in entry.name
                   or any([note.content for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))

    def find_by_pattern(self, pattern):
        # Use a comprehension to grab all entries that have a title or
        # note content matching the given pattern
        matches = [entry for entry in self.entries
                   if re.search(pattern, entry.name) is not None
                   or any([re.search(pattern, note.content)
                           for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))
