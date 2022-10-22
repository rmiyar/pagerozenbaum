from django.db import models
from django.contrib.auth.models import  User

class Home(models.Model):
    usuario =  models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 null = True,
                                 blank= True )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField( null = True,
                                    blank= True)
# Create your models here.
