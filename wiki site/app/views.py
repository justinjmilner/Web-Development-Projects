from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_detail(request, entry):
    
    content = util.get_entry(entry)
    content = util.convert(content)
    if content is None:
        return render(request, "encyclopedia/index.html", {
            "error": "ERROR",
            "message": f"The wiki entry for {entry} does not exist."
        })
    else:
        return render(request, "encyclopedia/layout.html", {
            "title": entry,
            "content": content,
            "entries": util.list_entries() 
        })

def search(request):
    if request.method == "POST":
        query = request.POST.get("q", "")
        if query:
            results = []
            entries = util.list_entries()
            for entry in entries:
                if query.lower() == entry.lower():
                    return entry_detail(request, entry)
                if query.lower() in entry.lower():
                    results.append(entry)
            if results:
                return render(request, "encyclopedia/search.html", {
                    "entries" : results
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "message": f"No wiki entries found for {query}"
                })
    return index(request)

def create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        exists = util.get_entry(title)
        body = request.POST.get("body")
        if exists:
            return render(request, "encyclopedia/create_page.html", {
                "error": "Error: Wiki entry already exists"
            })
        util.save_entry(title, body)
        return HttpResponseRedirect(reverse("encyclopedia:entry_detail", args=[title]))
            
    return render(request, "encyclopedia/create_page.html")

def edit_page(request, title):
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save") == "Save changes":
            body = request.POST.get("body")
            util.save_entry(title, body)
            return HttpResponseRedirect(reverse("encyclopedia:entry_detail", args=[title]))
        elif request.POST.get("edit") == "Edit Page":   
            content = request.POST.get("body")
            return render(request, "encyclopedia/edit_page.html", {
                "content": content,
                "title": title
            })
        
def random_wiki(request):
    titles = util.list_entries()
    title = random.choice(titles)
    return HttpResponseRedirect(reverse("encyclopedia:entry_detail", args=[title]))

