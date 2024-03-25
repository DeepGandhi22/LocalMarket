from django.db.models import Q
from LocalMarket.LocalMarket.models import Product

def searchproducts(request, pk):

    search_query = ('')

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    # products = Product.objects.filter(shop_id=pk)
    products = Product.objects.distinct().filter(product_name__icontains=search_query, shop_id=pk)

    return products, search_query