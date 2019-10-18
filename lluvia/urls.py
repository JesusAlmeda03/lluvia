"""lluvia URL Configuration

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
from django.urls import path
from inicio import views as inicio_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path ('inicio/', inicio_views.login_view, name = "login"),
    path ('/', inicio_views.login_view, name = "login"),
    path ('inicio/login/', inicio_views.login_view, name = "login"),
    path ('inicio/mensaje/', inicio_views.mensaje_view, name = "mensaje"),
    path ('inicio/dash/', inicio_views.dash_view, name = "dash"),
    path ('inicio/nuevo/', inicio_views.nuevo_view, name = "nuevo"),
    path ('inicio/mensaje_error/', inicio_views.mensajeerror_view, name = "error"),
    path ('inicio/logout/', inicio_views.logout_view, name = "logout"),
]
