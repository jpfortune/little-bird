"""bridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from upload.views import image_upload

from rest_framework import routers
from api import views as api_views
from telegram import views as telegram_views

router = routers.DefaultRouter()
router.register(r"records", api_views.RecordViewSet)
router.register(r"api/records", api_views.RecordViewSet)

router.register(r"telegram", telegram_views.ChannelViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path(
    #    "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    # ),
    # path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
