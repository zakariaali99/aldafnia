from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
from .models import NewsArticle, Certificate

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title',)
