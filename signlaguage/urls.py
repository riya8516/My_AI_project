"""
URL configuration for signlaguage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from signlanguageapp import views


urlpatterns = [
    

    path("",views.register,name="register"),

    path("login/",views.login,name="login"),

    path("Home/",views.Home,name="Home"),

    path("logout/",views.logout,name="logout"),

    path("login/",views.login,name="logoin"),

    path("about/",views.about,name="about"),

    path("features/",views.features,name="features"),

    path("detection/",views.detection,name="detection"),

    path("contact/",views.contact,name="contact"),

]
