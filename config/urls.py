from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from fabrica_needs.views import EntryViewSet, OutflowViewSet, ProductViewSet, UserViewSet , WalletViewSet

router = DefaultRouter()
router.register(r"entries", EntryViewSet)
router.register(r"outflows", OutflowViewSet)
router.register(r"products", ProductViewSet)
router.register(r"wallet", WalletViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
