from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product, Specification

class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SpecificationInline]
