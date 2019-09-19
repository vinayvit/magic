# insta_project/urls.py
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.views.generic.base import TemplateView
from django.conf.urls import include, url


urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('casino.urls')), # new
	path('contact/', include('sendemail.urls'), name='contact'),
	path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
	 path('accounts/', include('django.contrib.auth.urls')), # new

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
	
	