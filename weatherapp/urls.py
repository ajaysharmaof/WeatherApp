
from django.contrib import admin
from django.urls import path, include
#murphy 1221
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')),
]
