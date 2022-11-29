from django.contrib import admin
from .models import User, Auction_Listing, Bids, Comments

# Register your models here.

admin.site.register(User)
admin.site.register(Auction_Listing)
admin.site.register(Bids)
admin.site.register(Comments)
