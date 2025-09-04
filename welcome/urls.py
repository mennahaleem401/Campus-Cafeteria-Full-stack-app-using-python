from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update-order/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('place_order/', views.place_order, name='place_order'),
    path("customer/", views.customer_dashboard, name="customer_dashboard"),
    path('admin/order/<int:order_id>/update/', views.update_order_status, name='update_order_status'),

]