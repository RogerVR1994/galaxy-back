from django.db import models

class Participant(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    manager = models.CharField(max_length=60)
    type_of_participant = models.CharField(max_length=60)
    foundation_date = models.DateField()

    def __str__(self):
        return self.name