from modeltranslation.translator import register, TranslationOptions
from .models import NewsArticle, Certificate

@register(NewsArticle)
class NewsArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
