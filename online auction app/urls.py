from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing, name="create_listing"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("add-watchlist/<str:listing_id>", views.add_watchlist, name="add_watchlist"),
    path("remove-watchlist/<str:listing_id>", views.remove_watchlist, name="remove_watchlist"),
    path("bid/<str:listing_id>", views.update_bid, name="bid"),
    path("close/<str:listing_id>", views.close, name="close"),
    path("comment/<str:listing_id>", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.category, name="category")
]
