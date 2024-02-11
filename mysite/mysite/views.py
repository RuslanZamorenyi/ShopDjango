from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import AddBrand, AddSize, AddColour, AddToBucket
from .models import Sizes, Names, Colours


def home_page(request):
    return render(request, 'home_page.html')

@csrf_protect
@login_required
def choose_brand(request):
    list_sizes = Sizes.objects.all()
    list_colours = Colours.objects.all()
    list_brands = Names.objects.all()
    context = {"list_sizes": list_sizes,
               'list_brands': list_brands,
               'list_colours': list_colours}
    current_user = request.user
    print(current_user.id)
    if request.method == 'POST':
        form = AddToBucket(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            data = form.save()

            print(data)
            data.current_user = current_user
            data.save()

            return redirect('home_page')
    else:
        form = AddBrand
        print("dkf")

    return render(request, 'choose_brand_size_colour.html', context=context)



def add_brand(request):
    print(request.method)
    if request.method == 'POST':
        print("dfskldfj")
        form = AddBrand(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AddBrand

        return render(request, 'add_brand.html')


def add_size(request):

    print(request.method)
    if request.method == 'POST':
        print("ро")
        form = AddSize(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()

            return redirect('home_page')
    else:
        form = AddSize()
        return render(request, 'add_size.html')


def add_colour(request):
    print(request.method)
    if request.method == 'POST':
        print("ро")
        form = AddColour(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()

            return redirect('home_page.html')
    else:
        form = AddColour()
        return render(request, 'add_colour.html')