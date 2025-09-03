from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment, Request

def home(request):
    return render(request, 'rental/home.html')

def catalog(request):
    items = Equipment.objects.all()
    if request.method == "POST":
        Request.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message", "")
        )
        return redirect("request_success")
    return render(request, "rental/equipment_list.html", {"items": items})

def equipment_detail(request, pk):
    item = get_object_or_404(Equipment, pk=pk)
    return render(request, 'rental/equipment_detail.html', {"item": item})

def about(request):
    return render(request, 'rental/about.html')

def contacts(request):
    if request.method == "POST":
        return render(request, 'rental/request_success.html')
    return render(request, 'rental/request_form.html')

def request_success(request):
    return render(request, 'rental/request_success.html')
