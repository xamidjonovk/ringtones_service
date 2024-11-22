from django.db import models
from django.core.files.storage import FileSystemStorage


# Models
class Ringtone(models.Model):
    letter = models.CharField(max_length=1)
    name = models.CharField(max_length=100, db_index=True)
    gender = models.IntegerField(choices=[(0, 'Boys'), (1, 'Girls')])
    ringtone_file = models.FileField(storage=FileSystemStorage(location='media/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.letter}"
