from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Cart
from products.models import AllProducts
from django.contrib import messages

# Create your views here.


def your_cart(request):
    if request.method == 'POST':
        fromWhere = request.POST.get('fromHere')
        product_id = request.POST.get('cart_product_Id')
        product_quantity = request.POST.get('cart_product_Quantity')
        product_size = request.POST.get('cart_product_Pack')
        product = AllProducts.objects.get(products_id=product_id)
        # getting the number of product with id and user
        existed_product = Cart.objects.filter(user=request.user, product_id_cart=product_id).count()

        if existed_product == 0:
            # here icecream is added normally if this is a new icecream in user's cart.
            print('first one')
            Cart.objects.create(
                item=product,
                size=product_size,
                quantity=product_quantity,
                price=product.product_price,
                user=request.user,
                session_key=request.session.session_key,
                product_id_cart=product.products_id
            )
            messages.success(request, "Added to Cart Successfully")
            if fromWhere == "allproductspage":
                return redirect('products')
            elif fromWhere == "homepage":
                return redirect('home:home')
            else:
                return redirect(f'/stock/products/{product.product_slug}') # type: ignore
        
        if existed_product != 0:
            # here icecream quantity is added if this is not a new icecream in user's cart.           
            target_product = Cart.objects.filter(user=request.user, product_id_cart=product_id)[0]
            x = target_product.quantity
            y = str(int(x) + int(product_quantity))
            tpu = Cart.objects.filter(user=request.user, product_id_cart=product_id)[0]
            tpu.quantity = y
            tpu.save()
            messages.success(request, "Cart Item Updated Successfully")
            if fromWhere == "allproductspage":
                return redirect('products')
            elif fromWhere == "homepage":
                return redirect('home:home')
            else:
                return redirect(f'/stock/products/{product.product_slug}') # type: ignore

    return render(request, 'needs/404.html')

def my_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'CartItems': cart_items, 'NoCartItems': cart_items}
    return render(request, 'cart/cart.html', context)

def deleteCartProduct(request):
    if request.method == "POST":
        deleteable = request.POST.get("DeleteThisIcecream")
        targetitem = Cart.objects.get(product_id_cart=deleteable, user=request.user)
        targetitem.delete()
        return redirect('my_cart')
    return render(request, 'needs/404.html')

def updateCart(request):
    if request.method == 'POST':
        targetProduct = request.POST.get('updated_cart_id')
        newQty = request.POST.get('updated_cart')
        theProduct = Cart.objects.filter(user=request.user, product_id_cart=targetProduct)[0]
        theProduct.quantity = newQty
        theProduct.save()
        return redirect('my_cart')
    return render(request, 'needs/404.html')