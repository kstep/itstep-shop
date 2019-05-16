from django import forms


class AddToCartForm(forms.Form):
    item_id = forms.IntegerField(min_value=1)
    amount = forms.IntegerField(min_value=1)