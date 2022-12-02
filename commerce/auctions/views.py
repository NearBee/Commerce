from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction_Listing


def index(request):
    return render(
        request, "auctions/index.html", {"listings": Auction_Listing.objects.all()}
    )


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)  # type: ignore
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(redirect_field_name="", login_url="login")
def create_listing(request):
    if request.method == "POST":
        lister = User.pk
        item_title = request.POST["title"]
        item_description = request.POST["description"]
        item_initial_price = request.POST["starting_bid"]
        item_picture = request.POST["item_picture"](request.POST, request.FILES)
        item_category = request.POST["item_category"]
        auction_listing = Auction_Listing.objects.create(
            item_title=item_title,
            item_description=item_description,
            item_initial_price=item_initial_price,
            item_picture=item_picture,
            item_category=item_category,
        )
        try:
            auction_listing.full_clean()
        except ValidationError as e:
            if e:
                return render(
                    request,
                    "auction/createlisting.html",
                    {
                        "title": item_title,
                        "description": item_description,
                        "starting_bid": item_initial_price,
                        "item_picture": item_picture,
                        "item_category": item_category,
                    },
                )

        # TODO: Continue working on Validation Error display
        # Also make sure that the listing isn't created if Validation Error shows up
        # Possibly create an ERROR page for the time being, better solution would be giving the forms back
        else:
            auction_listing.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/createlisting.html")


def active_listing(request, listing_key):
    # return render(request, "auctions/listing.html")
    pass
