from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Auth
    path('login/', views.DashboardLoginView.as_view(), name='login'),
    path('logout/', views.DashboardLogoutView.as_view(), name='logout'),

    # Home
    path('', views.index, name='index'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Specifications
    path('specifications/', views.specification_list, name='specification_list'),
    path('specifications/create/', views.specification_create, name='specification_create'),
    path('specifications/<int:pk>/update/', views.specification_update, name='specification_update'),
    path('specifications/<int:pk>/delete/', views.specification_delete, name='specification_delete'),

    # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # News
    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/update/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    # Certificates
    path('certificates/', views.certificate_list, name='certificate_list'),
    path('certificates/create/', views.certificate_create, name='certificate_create'),
    path('certificates/<int:pk>/update/', views.certificate_update, name='certificate_update'),
    path('certificates/<int:pk>/delete/', views.certificate_delete, name='certificate_delete'),

    # Messages
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
]
