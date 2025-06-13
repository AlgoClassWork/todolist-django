from django.db import models

# Create your models here.
class Task(models.Model):

    title = models.CharField('Название задачи', max_length=200 )
    completed = models.BooleanField('Завершено', default=False )
    created_at = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return self.title

