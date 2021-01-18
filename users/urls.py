from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('say/', views.say, name='say'),
    path('birthday/<int:year>/<int:month>/', views.birthday, name='birthday'),
    path('sends_get/', views.sending_get, name='sends_get'),
    path('sends_post/', views.sending_post, name='sends_post'),
    path('sends_json/', views.sends_json, name='sends_json'),
    path('set_cookies/', views.set_cookies, name='set_cookies'),
    path('get_cookies/', views.get_cookies, name='get_cookies'),
    path('set_session/', views.set_session, name='set_session'),
    path('checking/', views.checking, name='checking'),
    path('checkview/', views.Checking.as_view(), name='checkview'),
    path('addview/', views.AddView.as_view(), name='addview'),
    path('detail/', views.detail, name='detail'),

]