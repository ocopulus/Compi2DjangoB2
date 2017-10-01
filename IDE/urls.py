from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loguin, name='loguin'),
    url(r'off/$', views.desconectar, name='desconectar'),
    url(r'index/$', views.index, name='index'),
    url(r'reporte/$', views.reporte, name='reporte'),
    url(r'ajax/usql/$', views.ejecutarUsql, name='ejecUsql'),
    url(r'ajax/tablas/$', views.traerTablas, name='traetablas'),
    url(r'ajax/ejecucion/$', views.traerEjecucion, name='traerEjecucion'),
    url(r'ajax/mensajes/$', views.taerMensajes, name='traerMensajes'),
    url(r'ajax/historial/$', views.taerHistorial, name='traerHistorial'),
    url(r'ajax/putoreporete/$', views.resolverReporete, name='traerReporte'),
    url(r'ajax/getUsuarios/$', views.getUsuarios, name='traerUsuarios'),
    url(r'ajax/getBD/$', views.getBD, name='traerBD'),
    url(r'ajax/getErrores/$', views.getErrores, name='traerErrores'),
    url(r'ajax/$', views.index2, name='ajax'),
    url(r'com/$', views.comunicacion, name = 'com')
]
