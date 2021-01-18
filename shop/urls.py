from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_out/', views.log_out, name='log_out'),
    
]