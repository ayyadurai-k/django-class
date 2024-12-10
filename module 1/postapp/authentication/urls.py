from django.urls import path
from authentication.views import signup_user, login_user, get_user

urlpatterns = [
    path('signup/', signup_user),
    path('login/', login_user),
    path('get/user/<int:id>/', get_user)
]
