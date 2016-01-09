from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^$', views.login, name='login'),  
  # url(r'^auth/$', views.auth_view, name='auth_view'),
  # url(r'^logout/$', views.logout, name='logout'),
  url(r'^mahasiswa/(?P<id_mhs>\d+)/$', views.mahasiswa, name='mahasiswa'),

]