from django.urls import path

from .forms import CustomUserChangePassForm
from .views import RegisterView, ProfileView, LoginView, LogoutView, ProfileUpdateView, CustomUserChangePassView

app_name='user'

urlpatterns=[
    path('regis/',RegisterView.as_view(),name='regis'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-user/', ProfileUpdateView.as_view(), name='update-profile'),
    path('change-pass/', CustomUserChangePassView.as_view(), name='change-pass')

]