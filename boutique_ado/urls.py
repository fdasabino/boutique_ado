from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from boutique_ado.settings import MEDIA_URL

admin.site.site_header = "BOUTIQUE-ADO ADMIN PORTAL"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("products/", include("products.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
