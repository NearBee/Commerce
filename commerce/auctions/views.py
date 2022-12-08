from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Auction_Listing
from .forms import create_listing_forms, bid_forms, comment_forms


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
        form = create_listing_forms(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            new_listing = form.save(commit=False)
            new_listing.user_id = request.user
            new_listing.save()

            return redirect("index")
    else:
        form = create_listing_forms()
    return render(request, "auctions/createlisting.html", {"form": form})


def active_listing(request, id):
    listing = Auction_Listing.objects.get(id=id)
    bids = bid_forms()
    comments = comment_forms()
    if not request.user.is_authenticated:
        return render(request, "auctions/listing.html", {"listing": listing})
    else:
        if request.method == "POST" and request.user.is_authenticated:
            bidding_form = bid_forms(request.POST)
            comment_form = comment_forms(request.POST)
            if bidding_form.is_valid() and comment_form.is_valid():
                new_bidding_form = bidding_form.save(commit=False)
                new_bidding_form.auction_id = request.auction_id
                new_bidding_form.user_id = request.user
                new_bidding_form.save()
                new_comment_form = comment_form.save(commit=False)
                new_comment_form.auction_id = request.auction_id
                new_comment_form.user_id = request.user
                new_comment_form.save()  # TODO: There has to be a cleaner way to do this possibly
                return render(
                    request,
                    "auctions/listing.html",
                    {
                        "listing": listing,
                        "bidding_form": bidding_form,
                        "comment_form": comment_form,
                    },
                )
            else:
                return render(
                    request,
                    "auctions/listing.html",
                    {
                        "listing": listing,
                        "bidding_form": bidding_form,
                        "comment_form": comment_form,
                    },
                )
    return render(
        request,
        "auctions/listing.html",
        {"listing": listing, "bidding_form": bids, "comment_form": comments},
    )
