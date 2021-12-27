from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 30, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Статья')
	cover = models.ImageField(upload_to='post_covers/', null=True, blank=True, default='post_covers/default.png')

	def __str__(self):
		return self.title
	

class Advertisement(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField()
	creation_date = models.DateField()
	view_num = models.IntegerField(default=6)
	
	def __str__(self):
		return self.title
	