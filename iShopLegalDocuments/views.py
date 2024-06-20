from django.shortcuts import render

# Create your views here.


def policy(request):
    return render(request, 'legal documents/policy.html')

def tandc(request):
    return render(request, 'legal documents/terms-and-conditions.html')

def support(request):
    return render(request, 'legal documents/support.html')