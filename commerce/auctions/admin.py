from django.contrib import admin
from .models import User, Auction_Listing, Bid, Comment

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(User)
admin.site.register(Auction_Listing)
admin.site.register(Bid)
admin.site.register(Comment, CommentsAdmin)
