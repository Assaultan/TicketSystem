from django.urls import path
from rest_framework.authtoken import views
from user_app.api.views import registration_view,logout_view

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('new/',registration_view,name ='register'),
    path('logout/',logout_view,name ='logout'),
]
