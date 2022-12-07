from django.urls import path
from django.conf.urls.static import static

from commerce import settings  # type: ignore
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="createlisting"),
    path("listing/<int:id>", views.active_listing, name="listing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
