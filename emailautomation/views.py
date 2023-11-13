from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm


def index(request):
    return render(request, 'index.html')


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = [form.cleaned_data['recipient']]
            send_mail(subject, message, 'your-email@gmail.com', recipient)
            return redirect('email_sent')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})


def email_sent(request):
    return render(request, 'email_sent.html')
