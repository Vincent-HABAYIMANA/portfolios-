from django.urls import path
from .import views
from myapp import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'), 
    path('request/<int:pk>', views.request, name='request'),
    path('signup/', views.signup, name='signup'),
    # path('login', login, name='login'),
    path('verify', views.verify, name='verify'),
    path('started/<int:pk>', views.started, name='started'),
    path('login', views.loginUser , name='login'),
    path('login', views.login , name='login'),
    path('dashboardUser/<int:pk>/', views.dashboardUser, name='dashboardUser'),
    path('dashboardAdmin', views.dashboardAdmin, name='dashboardAdmin'),
    path('collector/<int:pk>', views.collector, name='collector'),
     path('get-categories/', views.get_categories, name='get_categories'),
    path('paymentInfo', views.paymentInfo, name='payment'),
    path('submit_waste/', views.submit_waste, name='submit_waste'),
    path('get-paid//', views.get_paid, name='get_paid'),

    # chat
       path('update_status/<int:submission_id>/', views.update_status, name='update_status'),
    
    
    
     path('login/', views.role_login, name='role_login'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)