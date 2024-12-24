from django.urls import path
from authentication.views import create_profile, signup_user, login_user, get_user, update_profile

urlpatterns = [
    path('signup/', signup_user),
    path('login/', login_user),
    path('get/user/<int:id>/', get_user),
    path('create/profile/', create_profile),
    path('update/profile/', update_profile)
]
