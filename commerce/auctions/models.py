from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

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


class Auction_Listing(models.Model):
    lister = User.pk
    item_picture = models.ImageField(upload_to="images/")
    item_name = models.CharField(max_length=50)
    item_initial_price = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )


class Bids(models.Model):
    auction_id = Auction_Listing.pk
    user_id = User.pk
    new_bid = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000),
        ]
    )


class Comments(models.Model):
    auction_id = Auction_Listing.pk
    user_id = User.pk
    comments = models.TextField(
        max_length=255, help_text="Write a comment here about the item."
    )
