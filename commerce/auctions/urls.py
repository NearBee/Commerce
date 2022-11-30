from django.urls import path
from django.conf.urls.static import static

from commerce import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="creation"),
    path("<str:listing>", views.active_listing, name="listing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
