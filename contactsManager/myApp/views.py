from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Contact
from .forms import ContactForm

# Create your views here.
def view_contacts(request):
    search_query=request.GET.get('search','')
    contacts=Contact.objects.all().order_by('-created_date')
    #for search
    if search_query:
        contacts=contacts.filter(
            name__icontains=search_query
        )| contacts.filter(
            phone__icontains=search_query
        ) | contacts.filter(
            email__icontains=search_query
        )
    # pagination
    paginator=Paginator(contacts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj': page_obj,
        'search_query': search_query
    }
    return render(request,'contacts_list.html',context)

def add_contacts(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form=ContactForm()
    return render(request,'add_contacts.html',{'form':form})

def edit_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    if request.method=='POST':
        form=ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form .save()
            return redirect('contacts_list')
    else:
        form=ContactForm(instance=contact)
    return render(request,'edit.html',{'form':form})

def delete_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    if request.method=='POST':

        contact.delete()
        return redirect('contacts_list')
    return render(request, 'confirm_delete.html', {'contact': contact})