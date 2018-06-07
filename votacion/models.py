# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.


OPCIONES = (
    ('1','Socio'),
    ('2','Comite'),
)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voto = models.BooleanField(default=False)
    tipo_usuario = forms.ChoiceField(choices = OPCIONES)


class Informe(models.Model):
    codigo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

