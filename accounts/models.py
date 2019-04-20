from django.db import models
  
class expenses(models.Model):
      ammount     = models.FloatField()
      date        = models.DateField()
      time        = models.TimeField()
      place       = models.CharField(max_length = 50)
      discription = models.CharField(max_length = 100)
