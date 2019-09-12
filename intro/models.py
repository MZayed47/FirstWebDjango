from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    religion = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('intro:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " : " + self.status + " : " + self.age


class Degrees(models.Model):
    info = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=10)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.degree

