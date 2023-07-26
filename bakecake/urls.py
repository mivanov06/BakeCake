"""bakecake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cake_shop.views import index, lk, lk_order, cakes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lk/', lk, name='lk'),
    path('lk_order/', lk_order, name='lk_order'),
    path('cakes/', cakes, name='cakes')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
