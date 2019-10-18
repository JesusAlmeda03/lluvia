##Modelo para la lluvia de ideas

from django.db import models



class Participante(models.Model):
    IdParticipante = models.CharField(max_length = 50, blank = False),
    Nombre = models.CharField(max_length = 50)

class Respuestas(models.Model):
    IdRespuesta = models.IntegerField(max_length = 6, blank = False), 
    IdPregunta = models.IntegerField(max_length = 4, blank = False),
    IdParticipante = models.IntegerField(max_length= 5, blank = False),
