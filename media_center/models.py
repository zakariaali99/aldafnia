from django.db import models
from django.utils.translation import gettext_lazy as _

class NewsArticle(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    content = models.TextField(_("Content"))
    image = models.ImageField(_("Image"), upload_to='news/')
    published_date = models.DateField(_("Published Date"), auto_now_add=True)

    class Meta:
        verbose_name = _("News Article")
        verbose_name_plural = _("News Articles")
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    image = models.ImageField(_("Certificate Image"), upload_to='certificates/')
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

    def __str__(self):
        return self.title
