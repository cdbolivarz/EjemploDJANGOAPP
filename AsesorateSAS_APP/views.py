from django.shortcuts import render
from .models import *
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

def registroForm(req):
    return render(req, 'registro.html')

#Cotizar

def cotizarForm(req):
    return render(req, 'cotizar.html')

def cotizar(req):
    body = req.POST
    cotizacion = Cotizacion(
        id_estudiante = body['id_estudiante'],
        horas = body['horas'],
        id_categoria = body['id_categoria'],
    )
    cotizacion.save()
    return render(req, 'cotizar.html')
