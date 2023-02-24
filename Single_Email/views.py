from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import pandas as pd
# Create your views here.

def index(request):
    if request.method=="POST":

        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        #semail = request.POST.get('from_email')
        print(sub,msg,email)
        send_mail(sub, msg,'', [email])
        return render(request, 'Single_Email/Finished.html')
    return render(request, 'Single_Email/index.html')


