from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Listing, Watchlist, Bid, Comment
from .forms import CreateListingform, Watchlist, CreateBidform, CreateCommentform
import datetime

from .models import User

def index(request):
    if request.method == "POST":
        form = CreateListingform(request.POST)
        if form.is_valid():
            listing = Listing(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                bid=form.cleaned_data['bid'],
                url=form.cleaned_data['url'],
                category=form.cleaned_data['category'],
                user=request.user
            )
            listing.save()
            return HttpResponseRedirect(reverse("create_listing") + '?redirected_from=index')
    else:
        listings = Listing.objects.all()
        for listing in listings:
            bids = Bid.objects.filter(listing_id=listing.id)
            highest_bid = 0
            for bid in bids:
                if bid.bid > highest_bid:
                    highest_bid = bid.bid
                    listing.bid = highest_bid
        return render(request, "auctions/index.html", {
            'listings': listings,
        })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.GET.get('redirected_from') == 'index':
        return render(request, "auctions/create_listing.html", {
            "message": "Listing created!"
        })

    return render(request, "auctions/create_listing.html", {
        'form': CreateListingform()
    })

def listing(request, title):
    listing = Listing.objects.get(title=title)
    bids = Bid.objects.filter(listing_id=listing.id)
    highest_bid = 0
    winner = ""
    name = ""
    for bid in bids:
        if bid.bid > highest_bid:
            highest_bid = bid.bid
            winner = f" The winnner was {bid.winner}!"
            name = bid.winner
    if str(name) == str(request.user):
        winner = "You won!"
    if listing.closed == True:
        closed = f"This auction closed on {listing.closing_time}"
    else:
        closed = ""
    try:
        exists = Watchlist.objects.get(listing=listing, user=request.user.id)
    except:
        exists = None
    owner = listing.user
    if owner == request.user:
        pass
    else:
        owner = None
    comments_list = []
    comments = Comment.objects.filter(listing_id=listing.id)
    for comment in comments:
        comments_list.append(comment.comment)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist_exists": exists,
        "form": CreateBidform(),
        "owner": owner,
        "closed": closed,
        "winner": winner,
        "current_bid": highest_bid,
        "comments": comments_list,
        "comment_form": CreateCommentform(),
    })

@login_required
def add_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    watchlist = Watchlist(user=request.user, listing=listing)
    watchlist.save()
    return redirect('listing', title=listing.title)

@login_required
def remove_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    Watchlist.objects.filter(user=request.user, listing=listing).delete()
    return redirect('listing', title=listing.title)

@login_required
def update_bid(request, listing_id):
    if request.method == "POST":
        form = CreateBidform(request.POST)
        if form.is_valid():
            higher_bid=form.cleaned_data['bid']
            listing=Listing.objects.get(pk=listing_id)
            if higher_bid > listing.bid:
                bid_ = Bid(
                    bid=higher_bid, 
                    listing=listing,
                    user=request.user,
                    winner=request.user
                )
                listing.bid = higher_bid
                bid_.save()
                return redirect('listing', title=listing.title)
            else:
                listing = Listing.objects.get(pk=listing_id)
                return render(request, 'auctions/listing.html', {
                    "listing": listing,
                    "error": "*ERROR: A new bid must be greater than the current bid*"
                })

def close(request, listing_id):
    if request.method == "POST":
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d')
        listing = Listing.objects.get(pk=listing_id)
        listing.closing_time = now
        listing.closed = True
        listing.save()
        bid = Bid.objects.get(pk=listing_id)
        winner = bid.winner
        bids = Bid.objects.filter(listing_id=listing.id)
        for bid in bids:
            highest_bid = 0
            if bid.bid > highest_bid:
                highest_bid = bid.bid
        return render(request, 'auctions/listing.html', {
                    "listing": listing,
                    "closed": f"This auction closed on {listing.closing_time}",
                    "winner": f"The winner is: {winner}!",
                    "bid": highest_bid
                })

@login_required
def comment(request, listing_id):
    if request.method == "POST":
        form = CreateCommentform(request.POST)
        if form.is_valid():
            listing = Listing.objects.get(pk=listing_id)
            comment = Comment(
                user=request.user,
                listing=listing,
                comment=form.cleaned_data['comment']
            )
            comment.save()
            return redirect('listing', title=listing.title)
        else:
            listing = Listing.objects.get(pk=listing_id)
            return redirect('listing', title=listing.title)

@login_required
def watchlist(request):
    user = request.user
    watchlists = Watchlist.objects.filter(user=user)
    listings = []
    for watchlist in watchlists:
        listing = Listing.objects.get(id=watchlist.listing_id)
        listings.append(listing.title)
    return render(request, 'auctions/watchlist.html', {
        'user': user,
        'message': 'No listings on your watchlist',
        'listings': listings
    })

def categories(request): 
    listings = Listing.objects.all() 
    categories_ = []
    for listing in listings:
        if listing.closed:
            continue
        if listing.category:
            categories_.append(listing.category)
    return render(request, 'auctions/categories.html', {
        'categories': categories_,
        'message': 'No categories exist'
    })    

def category(request, category):
    listings = Listing.objects.all()
    listings_ = []
    for listing in listings:
        if listing.category.lower() == category:
            listings_.append(listing.title)
    return render(request, 'auctions/categories.html', {
    'listings': listings_,
    })
