from django.urls import path
from . import views
urlpatterns = [
  path('/hello' , views.hello, name = 'hello'),
  path('' , views.get_dist, name = 'dist'),
]