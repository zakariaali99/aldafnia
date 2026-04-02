from django.views.generic import ListView, DetailView
from .models import NewsArticle, Certificate

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'media_center/news_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['-published_date']

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'media_center/news_detail.html'
    context_object_name = 'article'

class CertificateListView(ListView):
    model = Certificate
    template_name = 'media_center/certificates.html'
    context_object_name = 'certificates'
    paginate_by = 12
