from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    reseña = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " | " + str(self.user.username)
