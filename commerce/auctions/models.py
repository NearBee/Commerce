from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# from django.forms import Textarea

# Remember that each time you change anything in auctions/models.py, you’ll need to first run python
# manage.py makemigrations and then python manage.py migrate to migrate those changes to your database.

# username = models.CharField(max_length=18)
# password = models.CharField(max_length=18)

# def __str__(self):
# // String representation of any username by user, easier readability
# return f"{self.id}: {self.username}"


class User(AbstractUser):
    username = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=18)
    email = models.CharField(max_length=30)
    timezone = models.CharField(max_length=255, blank=True)
    watchlist_item = models.ManyToManyField("Auction_Listing", related_name="watchers")

    def __str__(self):
        return self.username


class Auction_Listing(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    item_title = models.CharField(
        max_length=50,
        blank=False,
    )

    item_description = models.TextField(max_length=500, blank=False)

    item_initial_price = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        blank=False,
    )

    item_picture = models.ImageField(
        default="Double_Question_Mark.png",
    )

    CATEGORIES = (
        ("Electronics", "Electronics"),
        ("Toys", "Toys"),
        ("Home Essentials", "Home Essentials"),
        ("Fashion", "Fashion"),
        ("ETC.", "ETC."),
    )

    item_category = models.CharField(max_length=15, choices=CATEGORIES, blank=True)

    winner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
        related_name="winning_user",
    )

    def __str__(self):
        return self.item_title


class Bid(models.Model):
    auction_id = models.ForeignKey(
        Auction_Listing, on_delete=models.CASCADE, null=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    new_bid = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99999999),
        ],
        blank=False,
    )

    def __str__(self):
        return f"{self.auction_id}: {self.user} ${self.new_bid}"


class Comment(models.Model):
    auction_id = models.ForeignKey(
        Auction_Listing, on_delete=models.CASCADE, null=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    comments = models.TextField(
        max_length=500,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.comments
