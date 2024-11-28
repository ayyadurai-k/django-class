from django.urls import path
from authentication.views import signup_user

urlpatterns = [
    path('signup/', signup_user)
]
