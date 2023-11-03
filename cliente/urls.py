from django.urls import path, include
from .views.index import index
from .views.cuenta import CuentaViewSet
from .views.documento import DocumentoViewSet
from .views.index import SaludoView
from .views.emitir import EmitirView
from .views.generar import GenerarView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cuenta', CuentaViewSet)
router.register(r'documento', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("", index, name="index"),    
    path('emitir/', EmitirView.as_view(), name='servicio'),
    path('generar/', GenerarView.as_view(), name='generar'),
    path('saludo/', SaludoView.as_view(), name='saludo')
]