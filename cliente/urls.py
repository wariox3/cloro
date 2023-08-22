from django.urls import path
from .views.index import index
from .views.index import SaludoView

urlpatterns = [
    path("", index, name="index"),
    path('saludo/', SaludoView.as_view(), name='saludo')
]