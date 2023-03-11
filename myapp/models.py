from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=1, default='M')
    capacidades = models.CharField(max_length=200)
    habilidades = models.CharField(max_length=200)
    competencias = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def Human(self):
        return f"{self.name} {self.age} {self.sex}"
    
    def capacidades(self):
        if self.edad >= 18:
            if self.sexo == 'M':
                return ["Conducir", "Votar", "Trabajar"]
            else:
                return ["Conducir", "Votar", "Trabajar", "Ser madre"]
        else:
            return ["Estudiar", "Jugar", "Aprender"]

    def habilidades(self):
        if self.age >= 18:
            if self.sex == 'M':
                return ["Programar", "Diseñar", "Escribir"]
            else:
                return ["Programar", "Diseñar", "Escribir", "Pintar"]
        else:
            return ["Leer", "Dibujar", "Cantar"]

        Persona.add_to_class('habilidades', habilidades)


    def competencias(self):
        if self.age >= 18:
            if self.sex == 'M':
                return ["Liderazgo", "Comunicación", "Creatividad"]
            else:
                return ["Liderazgo", "Comunicación", "Creatividad", "Empatía"]
        else:
            return ["Curiosidad", "Colaboración", "Iniciativa"]

        Persona.add_to_class('competencias', competencias)


