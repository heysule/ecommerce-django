from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)
    supplier_price = forms.FloatField(label='Supplier Price')
    selling_price = forms.FloatField(label='Selling Price')
    stock = forms.IntegerField(label='Stock')
    image_url = forms.CharField(label='Image Url', max_length=2083)