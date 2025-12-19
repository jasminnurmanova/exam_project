from django.urls import path
from .views import RegisterView,ProfileView,LoginView,LogoutView
app_name='user'

urlpatterns=[
    path('regis/',RegisterView.as_view(),name='regis'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]