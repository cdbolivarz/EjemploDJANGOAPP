from django.db import models

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