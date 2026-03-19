from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"))
    location = models.CharField(_("Location"), max_length=200, blank=True)
    year = models.IntegerField(_("Year"), default=2024)
    image = models.ImageField(_("Main Image"), upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title
