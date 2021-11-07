from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
                    UserViewSet,
                    UserAPIView,
                    CategoryViewSet,
                    GenreViewSet,
                    TitleViewSet,
                    ReviewViewSet,
                    CommentViewSet,
                    )


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('users/me/', UserAPIView.as_view()),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
