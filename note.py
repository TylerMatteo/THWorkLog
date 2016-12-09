import datetime

class Note:

	def __init__(self, content):
		self.content = content
		self.createdAt = datetime.datetime.now()

	def __str__(self):
		return """{}\n- {}""".format(self.content, self.createdAt.strftime('%b %d, %Y - %H:%M:%S'))