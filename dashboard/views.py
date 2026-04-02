from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib import messages

from products.models import Category, Product, Specification
from projects.models import Project
from media_center.models import NewsArticle, Certificate
from core.models import ContactMessage
from .forms import CategoryForm, ProductForm, SpecificationForm, ProjectForm, NewsArticleForm, CertificateForm

def staff_required(user):
    return user.is_staff

@login_required
@user_passes_test(staff_required)
def index(request):
    context = {
        'stats': {
            'products': Product.objects.count(),
            'categories': Category.objects.count(),
            'projects': Project.objects.count(),
            'news': NewsArticle.objects.count(),
            'messages': ContactMessage.objects.count(),
        },
        'recent_messages': ContactMessage.objects.all()[:5],
        'recent_news': NewsArticle.objects.all()[:5],
    }
    return render(request, 'dashboard/index.html', context)

# Category Views
@login_required
@user_passes_test(staff_required)
def category_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    return render(request, 'dashboard/categories/list.html', {'categories': categories})

@login_required
@user_passes_test(staff_required)
def category_create(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة القسم بنجاح")
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {'form': form, 'title': 'إضافة قسم جديد'})

@login_required
@user_passes_test(staff_required)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث القسم بنجاح")
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {'form': form, 'title': f'تعديل القسم: {category.name}'})

@login_required
@user_passes_test(staff_required)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "تم حذف القسم بنجاح")
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': category, 'cancel_url': 'dashboard:category_list'})

# Product Views
@login_required
@user_passes_test(staff_required)
def product_list(request):
    products = Product.objects.all().select_related('category')
    return render(request, 'dashboard/products/list.html', {'products': products})

@login_required
@user_passes_test(staff_required)
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة المنتج بنجاح")
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/products/form.html', {'form': form, 'title': 'إضافة منتج جديد'})

@login_required
@user_passes_test(staff_required)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث المنتج بنجاح")
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/products/form.html', {'form': form, 'title': f'تعديل المنتج: {product.name}'})

@login_required
@user_passes_test(staff_required)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "تم حذف المنتج بنجاح")
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': product, 'cancel_url': 'dashboard:product_list'})

# Specification Views
@login_required
@user_passes_test(staff_required)
def specification_list(request):
    specifications = Specification.objects.all().select_related('product')
    return render(request, 'dashboard/specifications/list.html', {'specifications': specifications})

@login_required
@user_passes_test(staff_required)
def specification_create(request):
    form = SpecificationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة المواصفة بنجاح")
        return redirect('dashboard:specification_list')
    return render(request, 'dashboard/specifications/form.html', {'form': form, 'title': 'إضافة مواصفة جديدة'})

@login_required
@user_passes_test(staff_required)
def specification_update(request, pk):
    spec = get_object_or_404(Specification, pk=pk)
    form = SpecificationForm(request.POST or None, instance=spec)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث المواصفة بنجاح")
        return redirect('dashboard:specification_list')
    return render(request, 'dashboard/specifications/form.html', {'form': form, 'title': 'تعديل المواصفة'})

@login_required
@user_passes_test(staff_required)
def specification_delete(request, pk):
    spec = get_object_or_404(Specification, pk=pk)
    if request.method == 'POST':
        spec.delete()
        messages.success(request, "تم حذف المواصفة بنجاح")
        return redirect('dashboard:specification_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': spec, 'cancel_url': 'dashboard:specification_list'})

# Project Views
@login_required
@user_passes_test(staff_required)
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/projects/list.html', {'projects': projects})

@login_required
@user_passes_test(staff_required)
def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة المشروع بنجاح")
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/projects/form.html', {'form': form, 'title': 'إضافة مشروع جديد'})

@login_required
@user_passes_test(staff_required)
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث المشروع بنجاح")
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/projects/form.html', {'form': form, 'title': f'تعديل المشرع: {project.title}'})

@login_required
@user_passes_test(staff_required)
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "تم حذف المشروع بنجاح")
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': project, 'cancel_url': 'dashboard:project_list'})

# News views
@login_required
@user_passes_test(staff_required)
def news_list(request):
    news = NewsArticle.objects.all()
    return render(request, 'dashboard/news/list.html', {'news': news})

@login_required
@user_passes_test(staff_required)
def news_create(request):
    form = NewsArticleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة الخبر بنجاح")
        return redirect('dashboard:news_list')
    return render(request, 'dashboard/news/form.html', {'form': form, 'title': 'إضافة خبر جديد'})

@login_required
@user_passes_test(staff_required)
def news_update(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    form = NewsArticleForm(request.POST or None, request.FILES or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث الخبر بنجاح")
        return redirect('dashboard:news_list')
    return render(request, 'dashboard/news/form.html', {'form': form, 'title': f'تعديل الخبر: {article.title}'})

@login_required
@user_passes_test(staff_required)
def news_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "تم حذف الخبر بنجاح")
        return redirect('dashboard:news_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': article, 'cancel_url': 'dashboard:news_list'})

# Certificate Views
@login_required
@user_passes_test(staff_required)
def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'dashboard/certificates/list.html', {'certificates': certificates})

@login_required
@user_passes_test(staff_required)
def certificate_create(request):
    form = CertificateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تمت إضافة الشهادة بنجاح")
        return redirect('dashboard:certificate_list')
    return render(request, 'dashboard/certificates/form.html', {'form': form, 'title': 'إضافة شهادة جديدة'})

@login_required
@user_passes_test(staff_required)
def certificate_update(request, pk):
    cert = get_object_or_404(Certificate, pk=pk)
    form = CertificateForm(request.POST or None, request.FILES or None, instance=cert)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تم تحديث الشهادة بنجاح")
        return redirect('dashboard:certificate_list')
    return render(request, 'dashboard/certificates/form.html', {'form': form, 'title': f'تعديل الشهادة: {cert.title}'})

@login_required
@user_passes_test(staff_required)
def certificate_delete(request, pk):
    cert = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        cert.delete()
        messages.success(request, "تم حذف الشهادة بنجاح")
        return redirect('dashboard:certificate_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': cert, 'cancel_url': 'dashboard:certificate_list'})

# Message Views
@login_required
@user_passes_test(staff_required)
def message_list(request):
    messages_list = ContactMessage.objects.all()
    return render(request, 'dashboard/messages/list.html', {'messages_list': messages_list})

@login_required
@user_passes_test(staff_required)
def message_detail(request, pk):
    message_obj = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'dashboard/messages/detail.html', {'message_obj': message_obj})

@login_required
@user_passes_test(staff_required)
def message_delete(request, pk):
    message_obj = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        message_obj.delete()
        messages.success(request, "تم حذف الرسالة بنجاح")
        return redirect('dashboard:message_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': message_obj, 'cancel_url': 'dashboard:message_list'})

# Auth Views
class DashboardLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True

class DashboardLogoutView(LogoutView):
    next_page = reverse_lazy('dashboard:login')
