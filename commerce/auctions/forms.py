from django import forms
from .models import Auction_Listing, Bid, Comment


class create_listing_forms(forms.ModelForm):
    class Meta:
        model = Auction_Listing
        fields = "__all__"
        exclude = ["user_id"]


class bid_forms(forms.ModelForm):
    class Meta:
        model = Bid
        fields = "__all__"
        exclude = ["user_id", "auction_id"]


class comment_forms(forms.ModelForm):
    class Meta:
        model = Comment
        field = "__all__"
        exclude = ["user_id", "auction_id"]
