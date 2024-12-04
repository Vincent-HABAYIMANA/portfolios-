from django.urls import path
from .import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'), 
    path('request1', views.request1, name='request1'),
    path('signup', views.signup, name='signup'),
    # path('login', login, name='login'),
    path('verify', views.verify, name='verify'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('started', views.started, name='started'),
    path('login', views.loginUser , name='login'),
]
