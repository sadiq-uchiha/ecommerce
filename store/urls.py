from rest_framework import routers
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from .views import ProductViewSet,InventoryViewSet,OrderViewSet,CustomerViewSet,CustomerLoginView,UserproductView
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'order', OrderViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('userproduct/', UserproductView.as_view(), name='userproduct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
