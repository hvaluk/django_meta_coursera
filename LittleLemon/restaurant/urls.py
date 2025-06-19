from django.urls import path
from .views import index, MenuItemsView, MenuItemDetailView, test_view

urlpatterns = [
    path('', index, name="home"),
    path('test/', test_view, name='test'),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu_item'),
]