from django import forms
from django.forms import Textarea, NumberInput, TextInput, Select, ClearableFileInput
from .models import Auction_Listing, Bid, Comment


class create_listing_forms(forms.ModelForm):
    class Meta:
        model = Auction_Listing
        fields = "__all__"
        exclude = ["user", "winner"]
        widgets = {
            "item_title": TextInput(
                attrs={
                    "style": "height: 35px; width: 450px;",
                    "class": "form-control mt-2",
                }
            ),
            "item_description": Textarea(
                attrs={
                    "style": "height: 100px; width: 450px; resize: initial;",
                    "class": "form-control mt-2",
                }
            ),
            "item_initial_price": NumberInput(
                attrs={
                    "style": "height: 35px; width: 450px;",
                    "class": "form-control mt-2",
                }
            ),
            "item_category": Select(
                attrs={
                    "style": "height: 35px; width: 450px;",
                    "class": "form-control mt-2",
                }
            ),
            "item_picture": ClearableFileInput(
                attrs={
                    "style": "height: 35px; width: 450px;",
                    "class": "form-control mt-2",
                }
            ),
        }


class bid_forms(forms.ModelForm):
    class Meta:
        model = Bid
        fields = "__all__"
        exclude = ["user", "auction_id"]
        widgets = {
            "new_bid": NumberInput(
                attrs={"style": "height: 35px; width: 150px;", "class": "form-control"}
            ),
        }


class comment_forms(forms.ModelForm):
    class Meta:
        model = Comment
        field = "__all__"
        exclude = ["user", "auction_id"]
        widgets = {
            "comments": Textarea(
                attrs={
                    "style": "height: 100px; width: 100%; resize: initial;",
                    "class": "form-control",
                }
            ),
        }
