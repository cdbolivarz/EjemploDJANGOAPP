from django.db import models
from .validador import validar_entero


# Create your models here.
# Create your models here.
class Usuario(models.Model):
    nombre = models.TextField("Nombre completo",max_length=255,null = False)
    cedula = models.CharField("C.C.",primary_key=True,max_length=15,null = False)
    email = models.EmailField("Email",null = False)
    contrasena = models.CharField("Contrasena",max_length=50,null=False)
    telefono = models.TextField("Telefono",max_length=10,null=False)
    direccion = models.TextField("Direccion",max_length=255,null=True)
    nickname = models.CharField("Nombre de usuario",max_length=50)
    rol = models.TextField(max_length=10,null=False,choices=([('TT','tutor'),('EST','estudiante')]) )

    def __str__(self):
        return self.nickname


class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_estudiante = models.IntegerField(null= False)
    horas = models.IntegerField(null=False,validators=[validar_entero])
    id_categoria = models.TextField(null=False,
    choices=([('JR','JUNIOR'),('SB','SENIOR BASIC'),('SM','SENIOR MEDIUM'),
    ('SA1','SENIOR ADVANCED 1'),('SA2','SENIOR ADVANCED 2')]) )

    def get_precio(self):
        VALOR_HORA = {
            'JR':33000,
            'SB':44000,
            'SM':50000,
            'SA1':55000,
            'SA2':60000
        }
        return self.horas*VALOR_HORA[self.id_categoria]