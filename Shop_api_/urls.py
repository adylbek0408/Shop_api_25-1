"""
URL configuration for Shop_api_ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from product.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
    path('api/v1/categories/<int:id>/', CategoryDetailAPIView.as_view()),
    path('api/v1/products/', ProductsListAPIView.as_view()),
    path('api/v1/products/<int:id>/', ProductsDetailAPIView.as_view()),
    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('api/v1/products/reviews/', ReviewMoviesView.as_view()),
    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),
]