from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    

    path('category/<int:category_id>/', views.category_view, name='category'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('payment/', views.payment_view, name='payment'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),


    # Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    
    path('p1/', views.p1, name='p1'),
    path('p2/', views.p2, name='p2'),
    path('p3/', views.p3, name='p3'),
    path('p4/', views.p4, name='p4'),
    path('p5/', views.p5, name='p5'),
    path('p6/', views.p6, name='p6'),
    path('p7/', views.p7, name='p7'),
    path('p8/', views.p8, name='p8'),
    path('p9/', views.p9, name='p9'),
    path('p10/', views.p10, name='p10'),
    path('p11/', views.p11, name='p11'),
    path('p12/', views.p12, name='p12'),
    path('p13/', views.p13, name='p13'),
    path('payment/', views.payment, name='payment'),

    
]

