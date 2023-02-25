from django.shortcuts import render
from django.http import HttpResponse
#from django.core.mail import send_mail
import pandas as pd
import smtplib
# Create your views here.

def index(request):
    if request.method=="POST":
        login_email = request.POST.get('Login_Email')
        login_password = request.POST.get('Login_Password')
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(login_email,login_password)
        return render(request, 'Single_Email/Finished.html')
    return render(request, 'Single_Email/index.html')

class login():
    def login(request):
        return render(request, 'Single_Email/login.html')
        if request=="POST":
            login_email = request.POST.get('Login_Email')
            login_password = request.POST.get('Login_Password')
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(str(login_email),str(login_password))
            sub = request.POST.get('subject')
            msg = request.POST.get('message')
            email = request.POST.get('email')
            body = "Subject: {}\n\n{}".format(sub,msg)
            server.sendmail('demopython4311@gmail.com',email,body)
            server.quit()
            return render(request, 'Single_Email/index.html')
        return render(request, 'Single_Email/login.html')

        if request.method=="POST":
            sub = request.POST.get('subject')
            msg = request.POST.get('message')
            email = request.POST.get('email')
            body = "Subject: {}\n\n{}".format(sub,msg)
            server.sendmail('demopython4311@gmail.com',email,body)
            server.quit()
            return render(request, 'Single_Email/Finished.html')
        return render(request, 'Single_Email/index.html')


class email(login):
    pass