from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from .forms import VendorUserForm, ShopForm, ProductForm, ProfileVendorForm
from LocalMarket.models import Customer
from django.contrib.auth import views as auth_views
from .models import vendor, shop
from LocalMarket.models import Product
from .utils import searchproducts, finaltotal
# Create your views here.
from django.contrib.auth.decorators import login_required



# --------------- Vendor Profile VIEWS ----------------------

user_role = None
def loginVendor(request):

    page = 'login'
    user_auth = None
    #
    # if request.user.is_authenticated:
    #     return redirect('homepage')
    print("vendor")
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(username)
        # # username = username.lower()
        # password = request.POST.get('password')

        print(password)

        try:
            user = vendor.objects.get(username=username)
            print(user)
            user_auth = authenticate(request, username=username, password=password)
        except:
            print('vendor not found')
            # messages.error(request, "The Vendor not found!")

        if user_auth is not None:
            user_role = 'vendor'
            login(request, user_auth)
            return redirect('vendorprofile')

        else:
            print('Username or Password is incorrect')
            messages.error(request, "Username or Password is invalid!")

    return render(request, 'vendor/login_signup.html', {'page':page})

def createVendor(request):
    page = 'register'
    form = VendorUserForm()
    print(request)
    if request.method == 'POST':
        form = VendorUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            print(user)
            return redirect("loginVendor")
        else:
            messages.error(request, 'an error has occured while login')

    return render(request, 'vendor/login_signup.html', {'page':page, 'form':form})

def logoutVendor(request):
    logout(request)
    return redirect('loginVendor')


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

# --------------- Shop VIEWS ----------------------
@login_required(login_url='loginVendor')
def createShop(request):
    page = 'createShop'
    user_role = 'vendor'

    vendor_shop = vendor.objects.get(username=request.user.username)

    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.vendor_id = vendor_shop
            shop.save()
            messages.success(request, 'Shop was added successfully!')
            return redirect('homepage')

    return render(request, 'vendor/create_shop_product.html', {'page':page, 'form':form, 'user_role': user_role})

@login_required(login_url='loginVendor')
def editShop(request, pk):

    page = 'editShop'
    user_role = 'vendor'
    shop_e = shop.objects.get(shop_id=pk)
    form = ShopForm(instance=shop_e)

    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop_e)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shop changes saved successfully.')
            return redirect('vendorprofile')


    return render(request, 'vendor/edit_product_shop_vendor_form.html', {'form': form, 'user_role': user_role, 'page': page, 'shop_e': shop_e})

@login_required(login_url='loginVendor')
def createProduct(request, pk):
    page = 'createProduct'
    user_role = 'vendor'

    shop_p = shop.objects.get(shop_id=pk)
    # vendor_p = vendor.objects.get(username=request.user.username)

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.shop_id = shop_p
            product.save()

            messages.success(request, ' Product added successfully!')
            return redirect('shopview', pk=shop_p.shop_id)

    return render(request, 'vendor/create_shop_product.html', {'page': page, 'form': form, 'user_role': user_role})

@login_required(login_url='loginVendor')
def editProduct(request, pk):

    page = 'editProduct'
    user_role = 'vendor'
    product = Product.objects.get(product_id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            messages.success(request, 'Changes saved successfully.')
            return redirect('vendorprofile')


    return render(request, 'vendor/edit_product_shop_vendor_form.html', {'form': form, 'user_role': user_role, 'page': page})


@login_required(login_url='loginVendor')
def deleteProduct(request, pk):

    product = Product.objects.get(product_id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('vendorprofile')

    context = {'object': product}
    return render(request, 'delete_template.html', context)

