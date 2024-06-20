from django.shortcuts import render
from cart.models import Cart

# Create your views here.


def blogs(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems':cart_items}
    return render(request, 'blog/blogs.html', context)

def post_blogs(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems':cart_items}
    return render(request, 'blog/post.html', context)

def post_search(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems':cart_items}
    return render(request, 'blog/search.html', context)