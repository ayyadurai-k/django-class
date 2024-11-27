from django.urls import path, include
from posts.views import get_hello_world, PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'', PostViewSet)


urlpatterns = [
    path("get-hello-world/", get_hello_world),  # RUN THIS
    path("", include(router.urls))

    # LIST ALL - /posts/ - GET
    # CREATE - /posts/ - POST

    # GET ONE - /posts/21/ - GET
    # DELETE - /posts/21/ - DELETE
    # UPDATE - /posts/21/ - PATCH


]
