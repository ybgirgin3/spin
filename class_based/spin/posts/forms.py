from django import forms
# from django_prices.forms import MoneyField 
from django.utils.translation import gettext_lazy as _
from .models import PostModel


AVAILABLE_CURRENCIES = [("TL",_("TL")),("USD", _("USD"))]
CATEGORIES = [("İstanbul", _('İstanbul')), ('Sakarya', _('Sakarya'))]

class CreateNewPostForm(forms.ModelForm):
    
    title_field = forms.CharField(label="İlan Adı", max_length=50)
    about_field = forms.CharField(label="İlan Detayları")
    # price_field = MoneyField(label = "Fiyat", available_currencies=AVAILABLE_CURRENCIES)
    price_field = forms.DecimalField(label='Fiyat')
    currency_field = forms.ChoiceField(widget=forms.Select, choices=AVAILABLE_CURRENCIES)
    category_field = forms.ChoiceField(widget=forms.Select, choices=CATEGORIES)
    sold_or_not_field = forms.BooleanField(required=False)
    
    class Meta:
        model = PostModel
        fields = (
            'title_field',
            'about_field',
            'price_field',
            'currency_field',
            'category_field'
            # 'sold_or_not_field'
        )
     