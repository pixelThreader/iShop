from django.shortcuts import render, redirect
from django.db.models.functions import Length
from .models import Contact
from cart.models import Cart
from products.models import AllProducts
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('loginTheUserEmail')

    cart_items = Cart.objects.filter(user=request.user)
    GotTheTopProduct = AllProducts.objects.order_by('-product_totalOrders')[:3]
    GotSomeProduct = AllProducts.objects.annotate(name_length=Length(
        'product_name')).filter(name_length__lt=21).order_by('-product_name')[:4]
    context = {"TopProducts": GotTheTopProduct,
               "SomeProduct": GotSomeProduct, 'NoCartItems': cart_items}
    return render(request, 'home/index.html', context)


def about(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems': cart_items}
    return render(request, 'home/about.html', context)


def search(request):
    # search engine
    query = request.GET['query']

    if len(query) > 100:
        allProductsFoundviaSearch = AllProducts.objects.none()
    elif len(query) == 0:
        allProductsFoundviaSearch = AllProducts.objects.none()
    else:
        allProductTitle = AllProducts.objects.filter(
            product_slug__icontains=query)
        allProductsCategory = AllProducts.objects.filter(
            product_category__name__icontains=query)
        allProductDesc_sm = AllProducts.objects.filter(
            product_desc_sm__icontains=query)
        allProductDesc_lg = AllProducts.objects.filter(
            product_desc_lg__icontains=query)
        allProductsFoundviaSearch = allProductTitle.union(
            allProductDesc_sm, allProductDesc_lg, allProductsCategory)

    # if len(query) != 0 and allPost.count() == 0:
    #     messages.warning(request, 'No Post Found')

    cart_items = Cart.objects.filter(user=request.user)
    context = {
        'NoCartItems': cart_items,
        'SearchedItems': allProductsFoundviaSearch,
        'query': query}
    return render(request, 'home/search.html', context)


def settings(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems': cart_items}
    return render(request, 'home/settings.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name_contact")
        email = request.POST.get("email_contact")
        phone = request.POST.get("phone_contact")
        message = request.POST.get("message_contact")
        contactus = Contact(ContactUser=name, ContactPhone=phone, ContactEmail=email, ContactMessage=message)
        contactus.save()
        messages.success(request, 'Your Message Has Been Sent To Us!!')
        # get message text and level
        message_text = ''
        message_level = ''
        for message in messages.get_messages(request):
            message_text = str(message)
            message_level = message.level_tag
        return JsonResponse({'message_text': message_text, 'message_level': message_level})


    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems': cart_items}

    return render(request, 'home/contact.html', context)