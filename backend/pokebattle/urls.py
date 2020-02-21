from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import django_js_reverse.views

from battles.views import CreateBattleView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("", TemplateView.as_view(template_name="itworks.html"), name="home"),
    path("create/", CreateBattleView.as_view(), name="create_battle"),
]
