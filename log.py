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
            note = input('Please enter notes for this task. ' \
                         'Enter "q" to finish. ')
            if(note.upper() == "Q"):
                break;
            else:
                notes.append(note)
        self.entries.append(Entry(name, minutesDelta, notes))

    def lookup(self):
        pass
