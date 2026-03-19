from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("Image"), upload_to='categories/', blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name=_("Category"))
    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to='products/')
    features = models.TextField(_("Features"), help_text=_("One feature per line"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications', verbose_name=_("Product"))
    key = models.CharField(_("Specification Name"), max_length=100)
    value = models.CharField(_("Value"), max_length=200)

    class Meta:
        verbose_name = _("Specification")
        verbose_name_plural = _("Specifications")
