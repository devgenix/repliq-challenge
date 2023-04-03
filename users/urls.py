# Own Imports
from users import views

# Django Imports
from django.urls import path

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh_token/', views.CustomTokenRefreshView.as_view(), name='refresh_token'),
]
