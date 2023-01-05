import re

from django import forms
from django.forms import (
    ClearableFileInput,
    NumberInput,
    Select,
    Textarea,
    TextInput,
    Widget,
)
from django.utils.safestring import mark_safe

from .models import Auction_Listing, Bid, Comment


class Input_Group_Widget(Widget):
    """Widget that prepend boostrap-style span with data to specified base widget"""

    def __init__(self, base_widget, data, *args, **kwargs):
        """Initialize widget and get base instance"""
        super(Input_Group_Widget, self).__init__(*args, **kwargs)
        self.base_widget = base_widget(*args, **kwargs)
        self.attrs = kwargs.get("attrs")  # type: ignore
        self.data = data

    def render(self, name, value, attrs=None, renderer=None):
        """Render base widget and add bootstrap spans"""
        field = self.base_widget.render(name, value, attrs, renderer)

        if self.attrs.get("style"):
            style = f"style=\"{self.attrs['style']}\""
        else:
            style = ""

        if self.attrs.get("id"):
            id = f"{self.attrs['id']}"
        else:
            id = "id_item_initial_price"

        match = re.search(r"(?:type=\"(\w*)\")", field)
        if match:
            type = match.groups()[0]
        else:
            type = "text"

        return mark_safe(
            (
                f'<div class="input-group mb-3" {style}>'
                f'  <span class="input-group-text" id="{name}">{self.data}</span>'
                f'  <input type="{type}" id="{id}" class="form-control" value="{value}" name={name} aria-describedby="{name}">'
                f"</div>"
            )
        )


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
            "item_initial_price": Input_Group_Widget(
                base_widget=forms.NumberInput,
                data="$",
                attrs={
                    "style": "height: 35px; width: 450px;",
                    "placeholder": "$",
                    "class": "form-control mt-2",
                    "value": "1",
                },
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
