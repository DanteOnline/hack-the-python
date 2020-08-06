from django.db import models

from usersapp.models import BlogUser


class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Post(TimeStamp):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def has_image(self):
        return bool(self.image)

    def __str__(self):
        return f'{self.name}'
