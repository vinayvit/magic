from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView
from django.urls import path
from .views import IndexView

urlpatterns = [
url(r'^$',IndexView.as_view(),name="posttop"),
]

