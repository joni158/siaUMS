from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('identityApp.urls')),
    # url(r'', include('khsApp.urls')),
    # url(r'', include('krsApp.urls')),
    # url(r'', include('pbmApp.urls')),
    # url(r'', include('scheduleApp.urls')),
    # url(r'', include('wisudaApp.urls')),
]
