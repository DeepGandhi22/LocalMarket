from LocalMarket.models import Product
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'description', 'quantity', 'category']
        labels = {'product_name': 'Product Name',  'price': 'Price', 'description': 'Description', 'quantity': 'Quantity', 'category': 'Category'}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})