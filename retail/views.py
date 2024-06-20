from django.shortcuts import redirect, render
from django.http import HttpResponse
from cart.models import Cart
from products.models import AllProducts
from .models import Cupons, Info_Payment_for_one
from utilities.utilities import GenerateIdBig, GenerateDiscount, GenerateCuponId, numWordic, GenerateBarId
from utilities.genBAR import bar
from utilities.genQR import qr
# for precise discount calculations
from decimal import Decimal
# for async data response to template
from django.http import JsonResponse

# Create your views here.


def Checkout(request):
    if request.method == 'POST':
        forcupon = request.POST.get('forwhat')
        if forcupon == "CuponCode":
            code = request.POST.get('redeemcode')
            identity = request.POST.get('CuponId')
            MaxPrice = request.POST.get('MaxPrice')
            # getting which cupon is being used
            cuponIS = Cupons.objects.filter(
                cupon_user=request.user, cupon_code=code, cupon_id=identity)
            # checking cupon exist or not
            if cuponIS.count() == 0:
                getTheCupon = None
            else:
                getTheCupon = cuponIS[0]
            # Discount Calculations
            # calculate the discount amount
            if getTheCupon:
                Cupon_s_Code = getTheCupon.cupon_code
                Cupon_s_Discount = getTheCupon.cupon_discount
                Cupon_s_Discount = Decimal(getTheCupon.cupon_discount)
                MaxPrice = Decimal(request.POST.get('MaxPrice'))
                amount_left = (Cupon_s_Discount / 100) * MaxPrice
                discount_amount = amount_left.quantize(Decimal('.01'))
                payable_price = (
                    MaxPrice - discount_amount).quantize(Decimal('.01'))
                Valid = "Cupon Valid"
            else:
                Cupon_s_Code = 'Not a cupon'
                Cupon_s_Discount = 0
                MaxPrice = 0
                amount_left = 00
                discount_amount = 00
                payable_price = 00
                payable_price = float(MaxPrice)
                Valid = "Cupon Invalid"

            usedCupons = Cupons.objects.get(cupon_id=identity)
            usedCupons.cupon_used_status = "used"
            usedCupons.save()

            # Return the "getTheCupon" value as a JSON response
            return JsonResponse({'getTheCupon': str(getTheCupon), 'cupon_code': str(Cupon_s_Code), 'cupon_discount': str(Cupon_s_Discount), 'cupon_applied': str(discount_amount), 'youPay': payable_price, 'validity': str(Valid)})
        forpay = request.POST.get('forpay')
        # if forpay == "ToPayment":

    # utilities
    newcupons = Cupons.objects.filter(
        cupon_user=request.user, cupon_used_status='unused')
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems': cart_items,
               'NewCupons': newcupons}
    return render(request, 'retail/checkout.html', context)  # type: ignore


def cupons(request):
    newcupons = Cupons.objects.filter(
        cupon_user=request.user, cupon_used_status='unused')
    usedcupons = Cupons.objects.filter(
        cupon_user=request.user, cupon_used_status='used')
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NewCupons': newcupons,
               'UsedCupons': usedcupons,  'NoCartItems': cart_items}
    return render(request, 'retail/cupons.html', context)


def GenCupons(request):
    if request.method == 'POST':
        c_user = request.user
        c_id = GenerateIdBig(16)
        c_name = 'iShop Cupon'
        c_disc = GenerateDiscount()
        code = str(GenerateCuponId(c_name))
        c_code = code.upper()
        c_disc = GenerateDiscount()
        Cupons.objects.create(cupon_id=c_id, cupon_name=c_name,
                              cupon_user=c_user, cupon_discount=c_disc, cupon_code=c_code)
        return redirect(f'/retail/my-cupons/')

    return render(request, 'needs/404.html')


def TrashCupons(request):
    return render(request, 'needs/404.html')


def payment(request):
    return render(request, 'retail/payment.html')


def ToCheckoutOne(request):
    if request.method == "POST":
        forWhat = request.POST.get('forwhat')
        if forWhat == "ToCheckout":
            productIdentity = request.POST.get("buynow_product_Id")
            productis = AllProducts.objects.get(products_id=productIdentity)
            productQuantity = request.POST.get("buynow_product_Quantity")
            productSize = request.POST.get("buynow_product_Pack")

            # utilities
            newcupons = Cupons.objects.filter(
                cupon_user=request.user, cupon_used_status='unused')
            cart_items = Cart.objects.filter(user=request.user)
            context = {"productIdentity": productis,
                       "numberOfProduct": productQuantity, "productSize": productSize, 'NoCartItems': cart_items,
                       'NewCupons': newcupons}

            return render(request, "retail/checkout_one.html", context=context)
    return HttpResponse("This is the ToCheckoutOne view")


def Checkout_one(request):
    if request.method == 'POST':
        forWhat = request.POST.get('forwhat')
        if forWhat == "CuponCode":
            code = request.POST.get('redeemcode')
            identity = request.POST.get('CuponId')
            MaxPrice = request.POST.get('MaxPrice')
            # getting which cupon is being used
            cuponIS = Cupons.objects.filter(
                cupon_user=request.user, cupon_code=code, cupon_id=identity)
            # checking cupon exist or not
            if cuponIS.count() == 0:
                getTheCupon = None
            else:
                getTheCupon = cuponIS[0]
            # Discount Calculations
            # calculate the discount amount
            if getTheCupon:
                Cupon_s_Code = getTheCupon.cupon_code
                Cupon_s_Discount = getTheCupon.cupon_discount
                Cupon_s_Discount = Decimal(getTheCupon.cupon_discount)
                MaxPrice = Decimal(request.POST.get('MaxPrice'))
                amount_left = (Cupon_s_Discount / 100) * MaxPrice
                discount_amount = amount_left.quantize(Decimal('.01'))
                payable_price = (
                    MaxPrice - discount_amount).quantize(Decimal('.01'))
                Valid = "Cupon Valid"
            else:
                Cupon_s_Code = 'Not a cupon'
                Cupon_s_Discount = 0
                MaxPrice = 0
                amount_left = 00
                discount_amount = 00
                payable_price = 00
                payable_price = float(MaxPrice)
                Valid = "Cupon Invalid"

            usedCupons = Cupons.objects.get(cupon_id=identity)
            usedCupons.cupon_used_status = "used"
            usedCupons.save()

            # Return the "getTheCupon" value as a JSON response
            return JsonResponse({'getTheCupon': str(getTheCupon), 'cupon_code': str(Cupon_s_Code), 'cupon_discount': str(Cupon_s_Discount), 'cupon_applied': str(discount_amount), 'youPay': payable_price, 'validity': str(Valid)})

        if forWhat == "ToPayment":
            productIdentity = request.POST.get("buynow_product_Id")
            getProductOrder = AllProducts.objects.get(products_id=productIdentity)
            productQuantity = request.POST.get("buynow_product_Quantity")
            productSize = request.POST.get("buynow_product_Pack")
            user_fName = request.POST.get("firstName")
            user_lame = request.POST.get("lastName")
            user_phone1 = request.POST.get("phone1")
            user_phone2_alt = request.POST.get("phone2")
            user_email = request.POST.get("email")
            user_add_1 = request.POST.get("address")
            user_add_2 = request.POST.get("address2")
            user_country = request.POST.get("country")
            user_state = request.POST.get("state")
            user_pin = request.POST.get("pin")
            user_cupon_used = request.POST.get("cuponUsed")
            net_payable = request.POST.get("TotalPayableAmount")
            idIsGenerated = GenerateIdBig(6)
            baridIsGenerated = GenerateBarId(13)

            if user_cupon_used:
                appcpn = True
                cupon_is = Cupons.objects.get(cupon_code=user_cupon_used)
            else:
                appcpn = False
                cupon_is = None

            Info_Payment_for_one.objects.create(
                user_order_id=idIsGenerated,
                user_order_Code=baridIsGenerated,
                user_is_orderd=False,
                customer=request.user,
                user_order_nameFirst=user_fName,
                user_order_nameLast=user_lame,
                user_order_email=user_email,
                user_order_address1=user_add_1,
                user_order_address2_opt=user_add_2,
                user_order_country=user_country,
                user_order_state=user_state,
                user_order_pin=user_pin,
                user_order_phone1=user_phone1,
                user_order_phone2_opt=user_phone2_alt,
                user_order_cupon_applied=appcpn,
                user_order_cupon=cupon_is,
                user_order_product=getProductOrder,
                user_order_product_qty=productQuantity,
                user_order_product_size=productSize,
            )

            MY_Customer = Info_Payment_for_one.objects.get(
                user_order_id=idIsGenerated,
                user_order_Code=baridIsGenerated,
                customer=request.user,
                user_order_nameFirst=user_fName,
                user_is_orderd=False,
                user_order_nameLast=user_lame,
                user_order_email=user_email,
                user_order_address1=user_add_1,
                user_order_address2_opt=user_add_2,
                user_order_country=user_country,
                user_order_state=user_state,
                user_order_pin=user_pin,
                user_order_phone1=user_phone1,
                user_order_phone2_opt=user_phone2_alt,
                user_order_cupon_applied=appcpn,
                user_order_cupon=cupon_is,
                user_order_product=getProductOrder,
                user_order_product_qty=productQuantity,
                user_order_product_size=productSize,
            )
            myCustomer = {"customer":MY_Customer, "amountPay":net_payable}
            return render(request, 'retail/payment_one.html', context=myCustomer)

    # utilities
    newcupons = Cupons.objects.filter(
        cupon_user=request.user, cupon_used_status='unused')
    cart_items = Cart.objects.filter(user=request.user)
    context = {'NoCartItems': cart_items,
               'NewCupons': newcupons}
    return render(request, 'retail/checkout_one.html', context)


def payment_one(request):
    return render(request, 'needs/404.html')


def invoice(request):
    if request.method == "POST":
        methodOfPayment = request.POST.get("paymentMethod")
        # If Method is Visa
        if methodOfPayment == "Visa":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)

            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"VISA",
                "pmt_status":"Paid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is Debit Card
        elif methodOfPayment == "DebitCard":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)

            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"Debit Card",
                "pmt_status":"Paid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is Cash on delivery
        elif methodOfPayment == "COD":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)
            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"COD",
                "pmt_status":"Unpaid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is Master Card
        elif methodOfPayment == "MasterCard":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)

            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"Master Card",
                "pmt_status":"Paid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is PayPal
        elif methodOfPayment == "PayPal":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)

            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"PayPal",
                "pmt_status":"Paid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is Credit Card
        elif methodOfPayment == "PayPCreditCardal":
            shippingID = request.POST.get("BarCode")
            fname = request.POST.get("customerFirstName")
            lname = request.POST.get("customerLastName")
            add1 = request.POST.get("Address1")
            add2 = request.POST.get("Address2")
            phone1 = request.POST.get("customerPhone1")
            phone2 = request.POST.get("customerPhone2")
            LocationCountry = request.POST.get("Locationcountry")
            LocationState = request.POST.get("Locationstate")
            LocationCity = request.POST.get("Locationcity")
            LocationPin = request.POST.get("Locationpin")
            Product = request.POST.get("Product")
            Product_quantity = request.POST.get("iceCreamQuantity")
            Product_Price = request.POST.get("Product_net_Price")
            Product_sT = request.POST.get("serviceTax")
            Product_ship = request.POST.get("Shipping")

            # Generating Bar And QR
            
            #    >QR<
            name = str(str(fname.capitalize()) + " " + str(lname.capitalize()))
            orders = str(Product_quantity)
            location = str(LocationCountry + " (+91)")
            s = "Customer : " + name + "\nOrders : " + orders + "\nLocation : " + location + "\nProductShippingId : " + shippingID
            open("#iShopImportant docs/userTemp_QR.txt", "w").write(s)
            isname = str(fname) + str(request.user)
            isnamecontext = "iS" + str(fname) + str(request.user)
            qr(isname, "#iShopImportant docs/userTemp_QR.txt")

            #  >BAR<
            bar(shippingID, isname)

            # context sending
            fullname = fname + " " + lname
            address = add1 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            if add2 is None:
                add2=add1
            else:
                add2 = add2
            address2 = add2 + ", " + LocationCity + ", " + LocationState + ", " + LocationCountry + "("+ LocationPin +")"

            # Total amount
            price_in_words = numWordic(Product_Price)

            context = {
                "code" : isnamecontext,
                "name":fullname, 
                "address1":address, 
                "address2":address2,
                "phone":phone1, 
                "phone2":phone2,
                "serviceTax":Product_sT,
                "ShippingCharge":Product_ship,
                "total":Product_Price,
                "total_words":price_in_words,
                "pmt_method":"Credit Card",
                "pmt_status":"Paid",
                "product_name":Product
            }
            return render(request, 'retail/invoice.html', context=context)

        # If Method is Unknown Then Payment Not Accecpted
        else:
            return render(request, 'needs/403.html')



    return render(request, 'needs/404.html')
