from django.urls import path
from .views import  form_del_producto,form_mod_producto, form_producto, index,tienda,preventa,ver

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('preventa/', preventa, name='preventa'),
    path('form_producto/',form_producto,name="form_producto"),
    path('ver',ver,name="ver"),
    path('form_mod_producto/<id>',form_mod_producto,name="form_mod_producto"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)