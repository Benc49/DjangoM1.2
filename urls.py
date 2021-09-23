"""config URL Configuration

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
from app.views import hey
from app.views import age, total, int, random, lone_sum

urlpatterns = [
    path("lone-sum/<int:a>/<int:b>/<int:c>", lone_sum),
    path("near-hundred/<int:n>", int),
    path("string-splosion/<str>", random),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", total),
    path("hey/<name>", hey),
    path("age-in/<int:end>/<int:birthyear>", age),
    path('admin/', admin.site.urls),
]
