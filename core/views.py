
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # datos del formulario
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # contenido del email
            subject = f"New contact message from {name}"
            content = f"Phone: {phone}\nEmail: {email}\n\nMessage:\n{message}"

            # envío de email
            send_mail(subject, content, email, ['jacelrio@gmail.com'])  # <-- cambia esto

            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
