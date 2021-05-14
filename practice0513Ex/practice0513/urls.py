"""practice0513 URL Configuration

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
from django.contrib import admin
from django.urls import path
import crud2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud2.views.home, name="home"),
    path('<str:id>', crud2.views.detail, name='detail'),
    path('new/', crud2.views.new, name="new"),
    path('create/', crud2.views.create, name="create"),
    path('edit/<str:id>', crud2.views.edit, name = "edit"),
    path('update/<str:id>', crud2.views.update, name="update"),
]
