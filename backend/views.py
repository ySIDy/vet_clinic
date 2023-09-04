from django.shortcuts import render
from django.shortcuts import redirect
from backend.models import CustomerContact

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html", {})
    else:
        form = CustomerContact(
            user_name = request.POST["name"],
            phone = request.POST["phone"]
        )
        form.save()