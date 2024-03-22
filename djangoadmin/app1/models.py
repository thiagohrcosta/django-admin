from django.db import models

class User(models.Model):
  name = models.CharField('name', max_length=30)
  phone = models.BigIntegerField('phone')
  email = models.CharField('email', max_length=30)

  def __srt__(self):
    return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"