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
    path("cancel_auction/<int:listing_id>", views.cancel_auction, name="cancelauction"),
    path(
        "accept_auction_bid/<int:listing_id>",
        views.accept_auction_bid,
        name="acceptauctionbid",
    ),
    path("watchlist/<str:username>", views.watchlist, name="watchlist"),
    path("categories", views.all_categories, name="allcategories"),
    path("categories/<str:item_category>", views.categories, name="categories"),
    path("closedauctions", views.closed_auctions, name="closedauctions"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
