from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from category.views import CategoryViewSet
from order.views import OrderApiView
from product.views import ProductViewSet

from .drf_swagger import urlpatterns as doc_urls

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/orders/', OrderApiView.as_view()),
    path('api/v1/', include(router.urls)),
]

urlpatterns += doc_urls # swagger docs urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


