from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required



def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('success')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})


def success(request):
    return render(request, 'success.html')

def about(request):
    context={"data":False}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context={"data":True}
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('about')
            
    else:
        form = ContactForm()
    return render(request, 'about.html', {'form': form,'context':context})

def services(request):
    context={"data":False}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context={"data":True}
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('services')
            
    else:
        form = ContactForm()
    return render(request, 'services.html', {'form': form,'context':context})

def contact(request):
    context={"data":False}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context={"data":True}
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
            
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form,'context':context})
@login_required(login_url='/login')
def admin(request):
    items = Contact.objects.all()
    return render(request, 'admin.html', {'items': items})
    

   
