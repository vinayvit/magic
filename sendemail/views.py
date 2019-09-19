from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.shortcuts import render_to_response
from .forms import ContactForm
from django.contrib import messages
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']		
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['vinaykumar.vk2007@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                return HttpResponse('finaly done.')
    return render(request, "contact-us.html", {'form': form})

