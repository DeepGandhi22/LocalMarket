from django.shortcuts import render

# Create your views here.
@login_required(login_url='loginUser')
def customer_profile(request):

    user_role='customer'

    user = request.user
    print(user)
    customer = Customer.objects.get(username=user)
    print(customer)
    return render(request, 'LocalMarket/customer_profile.html', {'customer':customer, 'user_role': user_role})

@login_required(login_url='loginUser')
def edit_profile(request):

    user_role = 'customer'

    user = request.user
    customer = Customer.objects.get(username=user.username)
    form = ProfileForm(instance=customer)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=customer)
        print(form.is_valid())
        if form.is_valid():

            form.save()

            return redirect('homepage')

    context = {'form': form, 'customer': customer, 'user_role': user_role}
    return render(request, 'LocalMarket/profile_form.html', context)

@login_required(login_url='loginUser')
def checkout(request, pk):
    page = 'Checkout'
    order_item = Order.objects.get(order_id=pk, order_status='Ongoing')
    no_of_items = len(order_item.orderitem_set.all())
    delivery = 5
    amount = order_item.total_amount
    gst = amount * 0.13
    total = gst + delivery + amount
    user_role = 'customer'
    return render(request, 'LocalMarket/checkout.html',
                  {'page': page,'no_of_items': no_of_items, 'order_item': order_item, 'delivery': delivery, 'amount': amount,
                   'gst': gst, 'total': total, 'user_role':user_role})

@login_required(login_url='loginUser')
def checkout_confirmation(request, pk):
    order = get_object_or_404(Order, order_id=pk, order_status='Ongoing')
    if request.method == 'POST':
        order.order_status = 'Placed'
        order.save()
        return redirect(reverse('confirmation'))
    else:
        return redirect(reverse('checkout', args=[pk]))

@login_required(login_url='loginUser')
def confirmation(request):
    page = 'Confirmation'
    # order_item1 = Order.objects.get(order_id=pk,order_status='Placed')
    user_role = "customer"
    return render(request,'LocalMarket/confirmation.html',{'user_role': user_role, 'page': page})
