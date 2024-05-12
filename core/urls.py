from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from links_process.api.viewsets import LinksProcessViewSet
from playlists.api.viewsets import PlaylistsViewSet
from links.api.viewsets import LinkViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'playlists', PlaylistsViewSet)
router.register(r'links', LinkViewSet)
router.register(r'links-process', LinksProcessViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', views.obtain_auth_token),
    path('users/', include('users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]


urlpatterns += staticfiles_urlpatterns()