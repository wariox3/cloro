from django.urls import path
from .views.index import index
from .views.index import SaludoView
from .views.emitir import EmitirView

urlpatterns = [
    path("", index, name="index"),
    path('emitir/', EmitirView.as_view(), name='servicio'),
    path('saludo/', SaludoView.as_view(), name='saludo')
]