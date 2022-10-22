from django.urls import include, path, re_path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework_simplejwt import views

app_name = 'api'

jwt_patterns = [
    re_path(
        r"^jwt/create/?",
        views.TokenObtainPairView.as_view(),
        name="jwt-create"
    ),
    re_path(
        r"^jwt/refresh/?",
        views.TokenRefreshView.as_view(),
        name="jwt-refresh"
    ),
    re_path(
        r"^jwt/verify/?",
        views.TokenVerifyView.as_view(),
        name="jwt-verify"
    ),
]

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentViewSet,
    basename='comments'
)
v1_router.register(basename='follow', viewset=FollowViewSet, prefix='follow')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(jwt_patterns)),
]
