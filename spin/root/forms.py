from django import forms

# yeni item
class CreateNewItem(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    """
    owner = forms.CharField(label="username of the item owner", max_length=50)
    price = forms.DecimalField()
    """
    sold_or_not = forms.BooleanField(required=False)