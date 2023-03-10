from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report_builder/', include('report_builder.urls')),
    path('', include('application.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]