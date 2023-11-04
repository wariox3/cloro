from django.urls import path, include
from .views.index import index
from .views.cuenta import CuentaViewSet
from .views.documento import DocumentoViewSet
from .views.index import SaludoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cuenta', CuentaViewSet)
router.register(r'documento', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("", index, name="index"),    
    path('saludo/', SaludoView.as_view(), name='saludo')
]