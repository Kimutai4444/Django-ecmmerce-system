from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('category/<int:category_id>/', views.product_list_by_category, name='product_list_by_category'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.order_list, name='orders'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('category/<int:category_id>/products/', views.product_list, name='product_list_by_category_url'),
]