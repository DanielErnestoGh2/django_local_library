from django import forms
from .models import Sale, SaleItem, Product

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = []

class SaleItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()