from entry import Entry

import datetime

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
                break
            elif(option.upper() == "E"):
                break
            elif(option.upper() == "P"):
                break
            else:
                print("Invalid option, please try again.")

    def findByDate(self):
        pass

    def findByTimeSpent(self):
        pass

    def findByExactMatch(self):
        pass

    def findByPattern(self):
        pass
