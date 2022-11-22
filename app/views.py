from django.shortcuts import render
from .forms import detailsForm

# Create your views here.
# def index(request):
#     return render(request, "custdets.html")

def custdets(request):
    context = {}

    # create object of form
    form = detailsForm(request.POST or None, request.FILES or None)

    #check if the data is valid
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'custdets.html', context)

# introduce a redirect value here.
# add home page view

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')