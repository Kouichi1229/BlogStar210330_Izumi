from django.db import models
from datetime import datetime

class Blog_Posts(models.Model):
	
	title = models.CharField(max_length=200)
	content =   models.TextField()
	published_time = models.DateTimeField("date published",default=datetime.now())
	
	def __str__(self):
		return self.title