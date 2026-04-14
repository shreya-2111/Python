from django.shortcuts import render, redirect
from .models import Contact

#READ
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'contacts/list.html',{'contacts': contacts})

#CREATE
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        Contact.objects.create(name=name, phone=phone, email=email, address=address)
        return redirect('contact_list')
    return render(request,'contacts/add.html')

#UPDATE
def update_contact(request,id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.address = request.POST['address']
        contact.save()
        return redirect('contact_list')
    return render(request,'contacts/update.html',{'contact': contact})

#DELETE
def delete_contact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact_list')
