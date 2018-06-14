from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    types=(
    ('A', 'Inmobiliaria'),
    ('M', 'Vendedor independiente'),
    )
    tipo = models.CharField(max_length=30,choices=types)
    apellidoPaterno= models.CharField(max_length=30, blank=True)
    apellidoMaterno = models.CharField(max_length=30, blank=True)
    sex =  (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )
    sexo = models.CharField(max_length=30,choices=sex,blank=True)
    telefono = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15,blank=True)
    foto = models.ImageField(null=True)
    def definirCadena(self):
        cadena = "{0}, {1}, {2}, {3}"
        return cadena.format(self.nombre,self.apellidoPaterno,self.apellidoMaterno,self.sexo)
    def __str__(self):
        return self.definirCadena()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

