"""Nomina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("Apps.Home.urls")),
    path("AsientosContables/", include("Apps.AsientosContables.urls")),
    path("Deduciones/", include("Apps.Deduciones.urls")),
    path("Departamentos/", include("Apps.Departamentos.urls")),
    path("Empleados/", include("Apps.Empleados.urls")),
    path("Ingresos/", include("Apps.Ingresos.urls")),
    path("Puestos/", include("Apps.Puestos.urls")),
    path("Transacciones/", include("Apps.Transacciones.urls")),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
