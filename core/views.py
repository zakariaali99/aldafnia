from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import ContactMessage
from products.models import Product
from projects.models import Project
from media_center.models import NewsArticle, Certificate

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetching latest items for homepage presentation
        context['featured_products'] = Product.objects.all()[:4]
        context['recent_projects'] = Project.objects.all().order_by('-year', '-id')[:3]
        context['latest_news'] = NewsArticle.objects.all().order_by('-published_date')[:3]
        context['certificates'] = Certificate.objects.all()[:6]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, _("تم إرسال رسالتكم بنجاح. سنقوم بالرد عليكم في أقرب وقت ممكن."))
            return redirect('core:contact')
        
        messages.error(request, _("حدث خطأ أثناء إرسال الرسالة. يرجى التأكد من ملء جميع الحقول."))
        return self.get(request, *args, **kwargs)

class DesignSystemView(TemplateView):
    template_name = 'core/design_system.html'
