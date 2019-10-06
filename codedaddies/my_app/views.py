from django.shortcuts import render

def home(request):
    return render(request,"base.html")

def new_search(request):

    search=request.POST.get("search")
    stuff_for_frontend={
    "search":search,
    }


    return render(request, "my_app/new_search.html", stuff_for_frontend)


# Create your views here.
