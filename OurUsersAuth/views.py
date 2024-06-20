from django.contrib.auth.models import User

from retail.models import Cupons
from .models import AdditionalUserCredentials
from cart.models import Cart
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
import random
from django.contrib import messages

# Create your views here.


def signup(request):

    def GenerateRandomId(InputUsername):
        N = 3
        username = InputUsername
        alpha = '!@$%&?'
        numerics = '1234567890'
        res = ''.join(random.choices(username + alpha + numerics, k=N))
        generatedid = '91' + username[:5] + res
        return generatedid

    if request.method == 'POST':
        """
        Tip for file update:
        settings.py <--
        views.py <-- {request.FILES.get}                
        FormSendingHtml <-- 
        importants ⇾            _________↧↧⇓________________
        <form ... method="post" enctype="multipart/form-data">
        """
        profilePhoto = request.FILES.get('useravatar')
        print(profilePhoto)
        username = request.POST.get('userName')
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        birthbday = request.POST.get('userBirthDate')
        gender = request.POST.get('userGender')
        email = request.POST.get('userEmail')
        password = request.POST.get('userPassword')
        # CfrmPassword = request.POST.get('userPasswordConfirm')
        phone = request.POST.get('userPhone')
        phonealt = request.POST.get('userPhoneAlt')
        country = request.POST.get('userAddressCountry')
        state = request.POST.get('userAddressState')
        city = request.POST.get('userAddressCity')
        pincode = request.POST.get('userAddressZip')
        identity_1 = GenerateRandomId(username)
        identity_2 = GenerateRandomId(username)
        if identity_1 == identity_2:
            identity_2 = GenerateRandomId(username)

        user_now = User.objects.create_user(
            username=username, password=password, email=email, first_name=firstname, last_name=lastname)
        user = AdditionalUserCredentials(user=user_now, Emergency_id01=identity_1, Emergency_id02=identity_2, Avatar=profilePhoto, phone=phone, phone_alt=phonealt, gender=gender, birth=birthbday, country=country, state=state, city=city, pinCode=pincode)

        user.save()
        # Display a notification
        messages.success(request, firstname + "! Your Account Has Been Created Successfully.")
        return redirect("home:home")

    return render(request, 'authentication/signup.html')


def loginTheUserviaEmail(request):

    if request.method == 'POST':
        email = request.POST.get("login-email")
        password = request.POST.get("login-password01")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Display a notification
            messages.success(request, "Logged in Successfully via EMAIL.")
            return redirect("home:home")
        else:
            # Display a notification
            messages.warning(request, "Logged in Failed via EMAIL.")
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')


def loginTheUserviaUsername(request):

    if request.method == 'POST':
        username = request.POST.get("login-username")
        password = request.POST.get("login-password02")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Display a notification
            messages.success(request, "Logged in Successfully via USERNAME.")
            return redirect("home:home")
        else:
            messages.warning(request, "Logged in Failed via USERNAME.")
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')


def ForgetPassword(request):
    if request.method == 'POST':
        id_Gen = request.POST.get('FGPasswordGID')
        username = request.POST.get('FGPasswordUsername')
        Phone = request.POST.get('FGPasswordPhone')
        username_original = User.objects.get(username=username)
        if username_original is not None:
            id_Gen_original = username_original.additionalusercredentials.Emergency_id01
            Phone_original = username_original.additionalusercredentials.phone

            if id_Gen == id_Gen_original and Phone == Phone_original:
                request.session['TargetUsername'] = username
                return redirect("SetNewPassword")
            else:
                return render(request, 'authentication/forgtpwd.html')
        else:
            return render(request, 'authentication/forgtpwd.html')

    return render(request, 'authentication/forgtpwd.html')


def SetNewPassword(request):
    if request.method == 'POST':
        Password = request.POST.get('NewPassword')
        PasswordCon = request.POST.get('ConfirmNewPassword')
        if Password == PasswordCon:
            # Retrieve the value of 'TargetUsername' from the session
            username = request.session.get('TargetUsername')
            user = User.objects.get(username=username)
            user.set_password(Password)
            user.save()
            # Display a notification
            messages.success(request, username + "! Password Has Been Changed Successfully.")

            return redirect("home:home")
        else:
            # Display a notification
            messages.warning(
                request, username + "! Password Changing Configuration Failed. Try Again.")
            return render(request, 'authentication/forgtpwd.html')
    return render(request, 'authentication/setpwd.html')


def Profile(request):
    cart_items = Cart.objects.filter(user=request.user)
    cupons_left = Cupons.objects.filter(cupon_user=request.user).exclude(cupon_used_status="used")
    cupons_used = Cupons.objects.filter(cupon_user=request.user).exclude(cupon_used_status="unused")
    context = {'NoCartItems': cart_items, "cuponUsed":cupons_used, "cuponUnused":cupons_left}
    return render(request, 'authentication/profile.html', context)


def logoutTheUser(request):
    logout(request)
    # Display a notification
    messages.success(request, "Logged Out Successfully!")
    return redirect('home:home')
