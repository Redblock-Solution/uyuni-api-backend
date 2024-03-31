from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from links_process.api.viewsets import LinksProcessViewSet
from playlists.api.viewsets import PlaylistsViewSet
from links.api.viewsets import LinkViewSet

router = routers.DefaultRouter()
router.register(r'playlists', PlaylistsViewSet)
router.register(r'links', LinkViewSet)
router.register(r'links-process', LinksProcessViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()