"""nicetomeet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf.urls.static import static

from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth'))
]


"""используется только при локале, дает возможность подгружать файлы из /media/!!!"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)