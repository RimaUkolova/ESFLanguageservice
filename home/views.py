from django.core.mail import send_mail
# from .forms import FeedBackForm1, FeedBackForm2, FeedBackForm3
from .forms import FeedBackForm_1_Page
from esf.settings import base as settings
from django.http import HttpResponseRedirect
import re
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def feedback1(request):
    fake = False
    if request.method == 'POST':
        form = FeedBackForm_1_Page(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            match1 = re.match(r'admin', name, re.M)
            match2 = re.match(r'administrator', name, re.M)
            if match1 or match2:
                fake = True
            if not fake:
                message = "Chiamata dal " + cd['name'] + \
                          "\n Telefono: " + cd["phone"]
                send_mail(
                    cd['name'],
                    message,
                    settings.ADMIN_E_MAIL,
                    [settings.RECEIVER_E_MAIL],
                )
                return render(request, 'home/thanks.html')


def feedback2(request):
    fake = False
    if request.method == 'POST':
        form = FeedBackForm2(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            match1 = re.match(r'admin', name, re.M)
            match2 = re.match(r'administrator', name, re.M)
            if match1 or match2:
                fake = True
            if not fake:
                message = "Chiamata dal " + cd['name'] + \
                          "\n Telefono: " + cd["phone"] + "\n" + \
                          "\n Email: " + cd["email"] + "\n" + \
                          "Registrati per: " + cd["need_product"]
                        #   "Orario previsto: " + cd["time"] + " " + cd["date"]
                send_mail(
                    cd['name'],
                    message,
                    settings.ADMIN_E_MAIL,
                    [settings.RECEIVER_E_MAIL],
                )
                return render(request, 'home/thanks.html')
                

from django.http import JsonResponse
def feedback3(request):
    fake = False
    if request.method == 'POST':
        form = FeedBackForm3(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            match1 = re.match(r'admin', name, re.M)
            match2 = re.match(r'administrator', name, re.M)
            if match1 or match2:
                fake = True
            if True:
                message = "Chiamata dal " + cd['name'] + \
                          "\n Telefono: " + cd["phone"] + "\n" + \
                          "Registrati per: " + cd["need_product"]
                file = request.FILES['file']
                fs = FileSystemStorage()

                filename = fs.save(file.name.replace(" ", ""), file)
                email = EmailMessage(
                    cd['name'],
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.RECEIVER_E_MAIL])
                url = fs.url(filename)
                email.attach_file("/home/u7353/public_html/"+url)
                email.send()
                return JsonResponse({'furl':"/home/u7353/public_html/"+url})
