from django.shortcuts import render


@login_required(login_url='loginVendor')
def inventory(request, pk):
    page = 'inventory'
    user_role = 'vendor'

    shop_p = shop.objects.get(shop_id=pk)
    products, search_query = searchproducts(request, pk)
    return render(request, 'vendor/shopview_inventory.html',
                  {'page': page, 'shop': shop_p, 'products': products, 'search_query': search_query,
                   'user_role': user_role})

def shopview(request, pk):
    page = 'shopview'

    if request.user.is_authenticated:
        try:
            user_consumer = Customer.objects.get(username=request.user.username)
            user_role = 'customer'
        except:
            user_consumer = vendor.objects.get(username=request.user.username)
            user_role = 'vendor'
        print(user_consumer)
    print(user_role)

    shop_n = shop.objects.get(shop_id=pk)
    products, search_query = searchproducts(request, pk)
    return render(request, 'vendor/shopview_inventory.html', {'page':page, 'shop':shop_n, 'products':products, 'search_query':search_query, 'user_role': user_role})

@login_required(login_url='loginVendor')
def editprofileVendor(request):
    page = 'editProfileVendor'
    user_role = 'vendor'
    vendor_n = request.user
    vendor_v = vendor.objects.get(username=vendor_n.username)
    form = ProfileVendorForm(instance=vendor_v)

    if request.method == 'POST':
        form = ProfileVendorForm(request.POST, instance=vendor_v)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('vendorprofile')

    context = {'form': form, 'vendor': vendor_v, 'user_role': user_role, 'page': page}
    return render(request, 'vendor/edit_product_shop_vendor_form.html', context)


def vendorProfile(request):
    page = 'vendorProfile'
    user_role = 'vendor'
    vendor_user = vendor.objects.get(username=request.user.username)
    shops = vendor_user.shop_set.all()
    return render(request, 'vendor/vendorProfile.html', {'page':page, 'user_role':user_role, 'vendor_user':vendor_user, 'shops':shops})