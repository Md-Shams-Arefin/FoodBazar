from django.db import models


class Book_a_table(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    people = models.CharField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
