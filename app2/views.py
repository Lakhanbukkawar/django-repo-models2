from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request,"form.html")

def save(request):
    data={
        'name': request.POST.get('name'),
        'email': request.POST.get('email')
    }

    return render(request,"show.html",data)