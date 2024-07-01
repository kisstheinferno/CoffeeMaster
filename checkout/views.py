from django.shortcuts import render

def show_checkout(request):
    return render(request, "checkout/checkout.html")
