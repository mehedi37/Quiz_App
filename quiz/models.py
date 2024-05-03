from django.db import models

# Create your models here.


class quiz(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
