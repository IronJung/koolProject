from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('KPLInfo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]