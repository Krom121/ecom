from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SnippetForm


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you We will be in contact soon')
        return HttpResponseRedirect(reverse('home'))    
    form = SnippetForm()
    return render(request, "contact.html", {'form':form}, {'title': 'Contact'})

def list(request):
        return render(request, "list.html", {'title': 'blog'})

def product_list(request):
        return render(request, "shop/product/list.html", {'title': 'blog'})