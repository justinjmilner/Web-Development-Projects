from django.contrib import admin
from .models import User, Listing, Comment, Bid, Watchlist

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class ListingAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class BidAdmin(admin.ModelAdmin):
    pass

class WatchlistAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Watchlist, WatchlistAdmin)