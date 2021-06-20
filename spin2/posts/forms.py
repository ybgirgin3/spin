from django import forms
# from django_prices.forms import MoneyField 
from django.utils.translation import gettext_lazy as _


AVAILABLE_CURRENCIES = [("TL",_("TL")),("USD", _("USD"))]
CATEGORIES = [("İstanbul", _('İstanbul')), ('Sakarya', _('Sakarya'))]

class CreateNewPostForm(forms.Form):
    title_field = forms.CharField(label="İlan Adı", max_length=50)
    about_field = forms.CharField(label="İlan Detayları")
    # price_field = MoneyField(label = "Fiyat", available_currencies=AVAILABLE_CURRENCIES)
    price_field = forms.DecimalField(label='Fiyat')
    currency_field = forms.ChoiceField(widget=forms.Select, choices=AVAILABLE_CURRENCIES)
    category_field = forms.ChoiceField(widget=forms.Select, choices=CATEGORIES)
    # sold_or_not_form = forms.BooleanField()
    

    
    