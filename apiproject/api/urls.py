from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
)

router = DefaultRouter()

router.register("posts", PostViewSet, basename="posts")
router.register(
    r"^posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("", include(router.urls))
]
