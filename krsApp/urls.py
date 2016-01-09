from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^krs/(?P<id_mhs>\d+)/$', views.krs, name='krs'),

]