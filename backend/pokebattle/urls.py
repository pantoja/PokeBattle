from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import django_js_reverse.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", include("battles.urls")),
    path("", include("pokemon.urls")),
    path("", include("users.urls")),
]
