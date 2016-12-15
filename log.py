from entry import Entry

import re
import datetime
import pdb

class Log:

    def __init__(self):
        self.entries = []

    def new(self):
        name = input("What would you like to name this task? ")
        while True:
            try:
                minutes = input("How many minutes have you spent working on it? ")
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
        self.entries.append(Entry(name, minutesDelta, datetime.datetime.now(), notes))

    def lookup(self):
        while True:
            option = input("Would you like to lookup by [d]ate, [t]ime spent, [e]xact search, or [p]attern match? ")

            if(option.upper() == "D"):
                break
            elif(option.upper() == "T"):
                while True:
                    phrase = input("How many minutes spent are you searching for? ")
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

    def findByDate(self):
        pass

    def findByTimeSpent(self, minutes):
        pdb.set_trace()
        matches = [entry for entry in self.entries 
                   if entry.minutes == datetime.timedelta(minutes=minutes)]

        print("".join([str(entry) + '\n' for entry in matches]))

    def findByExactMatch(self, phrase):
        matches = [entry for entry in self.entries if phrase in entry.name 
                   or any([note.content for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))

    def findByPattern(self, pattern):
        matches = [entry for entry in self.entries if re.search(pattern, entry.name) is not None
                 or any([re.search(pattern, note.content) for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))
        
