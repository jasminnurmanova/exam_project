from django.urls import path
from .views import RegisterView

urlpatterns=[
    path('regis/',RegisterView.as_view(),name='regis')
]