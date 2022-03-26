from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from fornecedores.views import RegistrosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('registros', RegistrosViewSet, basename='Registros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
