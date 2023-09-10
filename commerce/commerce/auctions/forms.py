from django import forms
from .models import *

class CreateListingform(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    bid = forms.DecimalField(max_digits=10, decimal_places=2)
    url = forms.URLField(required=False)
    category = forms.CharField(max_length=50, required=False)

class CreateBidform(forms.Form):
    bid = forms.DecimalField(max_digits=10, decimal_places=2)

class CreateCommentform(forms.Form):
    comment = forms.CharField(label='', widget=forms.Textarea)


    