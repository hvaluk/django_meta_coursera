from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, about, book, reservations, bookings, test_view, MenuItemsView, MenuItemDetailView, msg, BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('reservations/', reservations, name="reservations"),
    path('bookings/', bookings, name='bookings'),
    path('test/', test_view, name='test'),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item'),
    path('message/', msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns += router.urls