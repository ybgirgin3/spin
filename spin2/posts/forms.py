from django import forms
from django_prices.forms import MoneyField 

AVAILABLE_CURRENCIES = ["TL", "USD"]
CHOICES = [('34', 'İstanbul'), ('54', 'Sakarya')]

class CreateNewPostForm(forms.Form):
    title_field = forms.CharField(label="İlan Adı", max_length=50)
    about_field = forms.CharField(label="İlan Detayları")
    price_field = MoneyField(label = "Fiyat", available_currencies=AVAILABLE_CURRENCIES)
    category = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    #sold_or_not_form = forms.BooleanField()
    

    
    