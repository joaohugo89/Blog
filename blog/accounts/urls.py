from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]