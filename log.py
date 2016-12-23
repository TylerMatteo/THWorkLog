from entry import Entry
from note import Note

import re
import datetime
import pdb

class Log:

    def __init__(self):

        self.entries = [
            Entry(
                'test1',
                datetime.timedelta(minutes=10),
                datetime.datetime(year=2016, day=11, month=12),
                ['test1 note']
            ),
            Entry(
                'test2',
                datetime.timedelta(minutes=20),
                datetime.datetime(year=2016, day=11, month=12),
                ['test2 note']
            ),
            Entry(
                'test3',
                datetime.timedelta(minutes=30),
                datetime.datetime(year=2016, day=12, month=12),
                ['test3 note']
            )
        ]

        #self.entries = []

    def new(self):
        name = input("What would you like to name this task? ")
        while True:
            try:
                minutes = input("How many minutes have you "
                    "spent working on it? ")
                minutesDelta = datetime.timedelta(minutes = int(minutes))
                break
            except ValueError:
                print("Invalid input. Please enter a number of minutes.")
        notes = []
        while True:
            noteText = input('Please enter notes for this task. ' \
                         'Enter "q" to finish. ')
            if(noteText.upper() == "Q"):
                break;
            else:
                notes.append(noteText)
        self.entries.append(Entry(name, minutesDelta, 
                            datetime.datetime.now(), notes))

    def lookup(self):
        while True:
            option = input("Would you like to lookup by [d]ate, "
                           "[t]ime spent, [e]xact search, "
                           "or [p]attern match? ")

            if(option.upper() == "D"):
                self.findByDate(datetime.datetime.now())
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
                self.findByTimeSpent(minutes)
            elif(option.upper() == "E"):
                phrase = input("What phrase would you like to search for? ")
                self.findByExactMatch(phrase)
                break
            elif(option.upper() == "P"):
                pattern = input("What regex would you like to search for? ")
                self.findByPattern(pattern)
                break
            else:
                print("Invalid option, please try again.")

    def findByDate(self, date):
        uniqueDates = list(set([entry.timestamp.date() for entry in self.entries]))
        sortedDates = sorted(uniqueDates)

        for i, date in enumerate(sortedDates):
            print("{}: {}".format(i+1, date.strftime('%b %d, %Y')))

        while True:
            try:
                dateSelection = int(input('Select a date to view by number. '))
                if(dateSelection in list(range(1, len(sortedDates)+1))):
                    break
                else:
                    print("That number isn't in the list of options. "
                          "Please try again.")
                    continue
            except ValueError:
                print('Not a valid input, please try again.')
                continue

        print("".join([str(entry) + '\n' for entry in self.entries
                      if entry.timestamp.date() == sortedDates[dateSelection - 1]]))

    def findByTimeSpent(self, minutes):
        matches = [entry for entry in self.entries 
                   if entry.minutes == datetime.timedelta(minutes=minutes)]

        print("".join([str(entry) + '\n' for entry in matches]))

    def findByExactMatch(self, phrase):
        matches = [entry for entry in self.entries if phrase in entry.name 
                   or any([note.content for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))

    def findByPattern(self, pattern):
        patternRaw = pattern.replace("\\", "\\\\")
        matches = [entry for entry in self.entries 
                   if re.search(patternRaw, entry.name) is not None
                   or any([re.search(patternRaw, note.content) 
                   for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))
        
