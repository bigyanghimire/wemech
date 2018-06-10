from django.db import models

# Create your models here.
class Job(models.Model):
	title=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	link=models.CharField(max_length=400)
	posted=models.DateTimeField()
	summary=models.TextField()
	company=models.TextField()


	def __str__(self):
		return self.title


class PostedJob(models.Model):
	title=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	summary=models.TextField()
	company=models.TextField()
	link=models.CharField(max_length=400)
	email=models.EmailField()

	def __str__(self):
		return self.title

class Email(models.Model):
	email=models.EmailField()


	def __str__(self):
		return self.email




