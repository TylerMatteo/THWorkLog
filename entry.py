from note import Note

class Entry:

	def __init__(self, name, minutes, timestamp, *notes):
		self.name = name
		self.minutes = minutes
		self.timestamp= timestamp
		for note in notes:
			self.addNote(note)

	def __str__(self):
		notesConcatenated = 
		return """{} - {}
			Time Spent: {}
			
		""".format(self.name, self.timestamp)

	def addNote(self, noteText):
		self.notes.append(Note(noteText))
		