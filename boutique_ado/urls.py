from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from boutique_ado.settings import MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("products/", include("products.urls")),
    path("bag/", include("bag.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
