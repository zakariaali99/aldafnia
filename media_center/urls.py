from django.urls import path
from . import views

app_name = 'media_center'

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('certificates/', views.CertificateListView.as_view(), name='certificates'),
]
