from django.urls import path
from .views import index, test_view, MenuItemsView, MenuItemDetailView, msg
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('', index, name="home"),
    path('test/', test_view, name='test'),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item'),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns += router.urls