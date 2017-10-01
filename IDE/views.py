from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from django.http import JsonResponse
import socket as sok
from random import randint
from . import Comunicacion

# Create your views here.
def loguin(request):
    if request.POST:
        us = request.POST['username']
        pas = request.POST['password']
        #Aqui enviamos los datos al servidor
        comunicador = Transferencia()
        alazar=randint(0,5001)
        contenido = '["validar":'+str(alazar)+', "login":"'+us+','+pas+'"]\n'
        respuesta = comunicador.comunicacion(contenido)
        parser = Comunicacion.Com()
        parser.accion(respuesta)
        if parser.login:
            request.session['us'] = us
            return redirect('index')
        else:
            raise Http404('Error Datos Invalidos')
    else:
        contexto = {
            'title':'Loguin',
            'year':datetime.now().year,
        }
        return render(request, "loguin.html", contexto)

def desconectar(request):
    request.session['us'] = ''
    comunicador = Transferencia()
    contenido = '["fin":"fin"]\n'
    respuesta = comunicador.comunicacion(contenido)
    return redirect('loguin')

def index(request):
    if request.session['us'] == '':
        raise Http404('No tienes acceso Inicia session')
    contexto = {
        'title':'principal',
        'year':datetime.now().year,
    }
    return render(request, "index.html",contexto)

def reporte(request):
    if request.POST:
        html = request.POST['txtresultado']
        return HttpResponse(html)
    else:
        contexto = {
            'title':'principal',
            'year':datetime.now().year,
        }
        return render(request, "reporte.html", contexto)

def resolverReporete(request):
    codigo = request.GET['txt']
    comunicador = Transferencia()
    contenido = '["reporte":"reporte","reporte":%%'+codigo+'%%]\n'
    print(contenido)
    respuesta = comunicador.comunicacion(contenido)
    print(respuesta)
    return HttpResponse(respuesta)

def getUsuarios(request):
    comunicador = Transferencia()
    contenido = '["getUsuarios":"getUsuarios"]\n'
    respuesta = comunicador.comunicacion(contenido)
    return HttpResponse(respuesta)

def getBD(request):
    comunicador = Transferencia()
    contenido = '["getBD":"getBD"]\n'
    respuesta = comunicador.comunicacion(contenido)
    return HttpResponse(respuesta)

def getErrores(request):
    codigo = request.GET['txt']
    comunicador = Transferencia()
    contenido = '["getErrores":"getErrores","codigo":%%'+codigo+'%%]\n'
    respuesta = comunicador.comunicacion(contenido)
    return HttpResponse(respuesta)

def ejecutarUsql(request):
    codigo = request.GET['txt']
    comunicador = Transferencia()
    contenido = '["usql":"usql","codigo":%%'+codigo+'%%]\n'
    respuesta = comunicador.comunicacion(contenido)
    return HttpResponse(respuesta)

def traerTablas(request):
    comunicador = Transferencia()
    contenido = '["tablas":"tablas"]\n'
    respuesta = comunicador.comunicacion(contenido)
    parser = Comunicacion.Com()
    parser.accion(respuesta)
    tablas = parser.tablas
    if tablas != None:
        return HttpResponse(tablas)
    return HttpResponse('')

def traerEjecucion(request):
    comunicador = Transferencia()
    contenido = '["ejecucion":"ejecucion"]\n'
    respuesta = comunicador.comunicacion(contenido)
    parser = Comunicacion.Com()
    parser.accion(respuesta)
    ejecucion = parser.ejecucion
    if ejecucion != None:
        return HttpResponse(ejecucion)
    return HttpResponse('')

def taerMensajes(request):
    comunicador = Transferencia()
    contenido = '["mensajes":"mensajes"]\n'
    respuesta = comunicador.comunicacion(contenido)
    parser = Comunicacion.Com()
    parser.accion(respuesta)
    mensajes = parser.mensajes
    if mensajes != None:
        return HttpResponse(mensajes)
    return HttpResponse('')

def taerHistorial(request):
    comunicador = Transferencia()
    contenido = '["historial":"historial"]\n'
    respuesta = comunicador.comunicacion(contenido)
    parser = Comunicacion.Com()
    parser.accion(respuesta)
    historial = parser.historial
    if historial != None:
        return HttpResponse(historial)
    return HttpResponse('')

def index2(request):
    #print(request.GET)
    print(request.GET['txt'])
    respuesta = {}
    respuesta['vida'] = 'sexo y amor'
    respuesta['sexo'] = 'never'
    respuesta['codigo'] = request.GET['txt']
    return HttpResponse(json.dumps(respuesta), content_type="application/json")

def comunicacion(request):
    HOST = "localhost"
    PORT = 5000
    alazar=randint(0,5001)
    print(str(alazar))
    sacar = '[ "validar": '+str(alazar)+' , "login": [\n"comando": "comando", "comando" : "comando"]]\n'
    sock = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(sacar.encode('utf-8'))
    sock.shutdown(1)
    data = sock.recv(2014)
    print(data.decode('ascii'))
    sock.close()
    return HttpResponse("extito papu")


class Transferencia:
    """Clase de para Manejar la comunicacion"""
    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 5000
    def comunicacion(self, sacar):
        sock = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
        sock.connect((self.HOST, self.PORT))
        sock.sendall(sacar.encode('utf-8'))
        sock.shutdown(1)
        tempdata = sock.recv(65500)
        self.data = tempdata.decode('ascii')
        sock.close()
        return self.data
