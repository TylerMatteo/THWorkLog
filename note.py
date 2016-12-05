import datetime

class Note:

	def __init__(self, content):
		self.content = content
		self.createdAt = datetime.datetime.now()

	def __str__(self):
		return """{}
				- {}""".format(self.content, self.createAt.strftime('%b %d, %Y - %H:%M:%S'))