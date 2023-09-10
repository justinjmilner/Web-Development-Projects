from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry_detail, name="entry_detail"),
    path("search", views.search, name="search"),
    path("create-page", views.create_page, name="create_page"),
    path("edit-page/<str:title>:", views.edit_page, name="edit_page"),
    path("random", views.random_wiki, name="random")
]
