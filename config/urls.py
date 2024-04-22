from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from fabrica_needs.views import EntryViewSet, OutflowViewSet, ProductViewSet, WalletViewSet

router = DefaultRouter()
router.register(r"entries", EntryViewSet)
router.register(r"outflows", OutflowViewSet)
router.register(r"products", ProductViewSet)
router.register(r"wallet", WalletViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
