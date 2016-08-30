from django.conf.urls import url,include
from apps.adopcion.views import	 SolicitudCreate, SolicitudList

urlpatterns =[

        url(r'^',SolicitudList.as_view(),name='index'),
        url(r'^solicitud/listar$',SolicitudList.as_view(),name='solicitud_listar'),
        url(r'^solicitud/nueva$',SolicitudCreate.as_view(), name='solicitud_crear'),

]

