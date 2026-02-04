from django import forms
from store.models import Product
# create your forms here

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.FloatField()
#     stock = forms.IntegerField()
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'name','price','stock'}