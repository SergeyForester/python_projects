"""p_5b9d932d9f URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import adminapp.views as adminapp
import mainapp.views as mainapp
import hashlib

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main_page, name='main'),
    path('room/<int:pk>/', mainapp.book_room, name='room'),
    path(f"management/{hashlib.sha256(mainapp.hotelName().encode('utf-8')).hexdigest()}/",
         include('adminapp.urls', namespace='s-admin'))]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
