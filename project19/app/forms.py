from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['pname','qty','price']

    def clean_qty(self):
        cleaned_data=super().clean()
        if cleaned_data.get('qty') <0:
            raise forms.ValidationError(message="qty value should be grather than 0")
        return cleaned_data['qty']
    
    