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

