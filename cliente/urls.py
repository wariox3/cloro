from django.urls import path
from .views.index import index
from .views.index import SaludoView
from .views.emitir import EmitirView
from .views.generar import GenerarView

urlpatterns = [
    path("", index, name="index"),
    path('emitir/', EmitirView.as_view(), name='servicio'),
    path('generar/', GenerarView.as_view(), name='generar'),
    path('saludo/', SaludoView.as_view(), name='saludo')
]