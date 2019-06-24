from django.shortcuts import render
from .models import Usuario
#from .serializables import UsuarioSerializer
from django.http import HttpResponse
import json

# Create your views here.
def registro(req):
    body = req.POST
    usuario = Usuario(
        nombre = body['nombre'],
        cedula = body['cedula'],
        email = body['email'],
        contrasena = body['contrasena'],
        telefono = body['telefono'],
        direccion = body['direccion'],
        nickname = body['nickname'],
        rol = body['rol']
    )
    usuario.save()
    return render(req, 'registro.html', {'usuario': usuario})

def registroFrom(req):
    return render(req, 'registro.html')
