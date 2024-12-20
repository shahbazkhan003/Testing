from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('api/products/', views.product_view, name='product_api'),
    path('api/product-detail/<int:pk>', views.product_detail_api, name='product-detail-api'),
    path('api/add-to-cart/', views.add_to_cart_api, name='add-to-cart'),
    path('api/cart/',views.show_cart,name='showcart'),
    path('api/pluscart/<int:pk>',views.plus_cart_api),
    path('api/minuscart/<int:pk>',views.minus_cart_api),
    path('api/removecart/<int:pk>',views.remove_cart_api),
    path('buy/', views.buy_now, name='buy-now'),
    path('api/profile/', views.profile_api, name='profile'),
    path('api/address/', views.address_api, name='address'),
    path('api/orders/', views.orders_api, name='orders'),
    path('api/changepassword/', views.change_password_api, name='changepassword'),
    path('api/mobile/', views.mobile_api, name='mobile'),
    path('api/mobile/<slug:data>', views.mobile_api, name='mobiledata'),
    path('api/laptop/', views.laptop_api, name='laptop'),
    path('api/laptopdata/<slug:data>', views.laptop_api, name='laptopdata'),
    path('api/topwear/', views.topwear_api, name='topwear'),
    path('api/buttomwear/', views.buttomwear_api, name='buttomwear'),
    path('api/registration/', views.customer_registration_api, name='customerregistration'),
    path('api/login/', views.login_api, name='login'),
    path('api/logout/', views.logout_api, name='logout'),
    path('api/newpassword/<str:email>/', views.new_password_api, name='newpassword'),
    path('api/checkout/', views.checkout_api, name='checkout'),
    path('api/paymentdone/', views.payment_done_api, name='paymentdone'),
    path('api/search/<int:pk>',views.search_api,name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)