from django.conf.urls import url,include
from apps.mascota.views import	index, mascota_view,mascota_list, mascota_edit,mascota_delete,Mascota_list,MascotaCreate
urlpatterns =[

		url(r'^$',index, name='index'),
      	url(r'^nuevo$',MascotaCreate.as_view(), name='mascota_crear'),
        url(r'^listar$',Mascota_list.as_view(), name='mascota_listar'),
        url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
        url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
]