from django.urls import path
from .views import index, detail, cv
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/',detail, name='detail'),
    path('cv/', cv, name='cv'),
]