from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField()

	def __str__(self):
		return self.title
		
class Date(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField()
	publication_date = models.DateField()
	
	def __str__(self):
		return self.title