from django import forms
from products.models import Category, Product, Specification
from projects.models import Project
from media_center.models import NewsArticle, Certificate
from core.models import ContactMessage

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'image', 'features']
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'features': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all', 'placeholder': 'أضف ميزة واحدة في كل سطر'}),
        }

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['product', 'key', 'value']
        widgets = {
            'product': forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'key': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'value': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description', 'location', 'year', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'year': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
        }

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'slug', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'slug': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'content': forms.Textarea(attrs={'rows': 8, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 focus:ring-2 focus:ring-primary outline-none transition-all'}),
        }
