from django.shortcuts import render
from django.http import HttpResponse
#from django.core.mail import send_mail
import pandas as pd
import smtplib
# Create your views here.

def index(request):
    if request.method=="POST":
        print(file)
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        #email = request.POST.get('email')
        e = pd.read_excel(request.POST.get('file'))
        emails = e['Emails'].values
        #contants = e['Contants'].values
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login('demopython4311@gmail.com','uxwmjnuunkycsjyl')
        #msg = f'{Name}Hello this is test'
        subject = "Hello word"
        for email in emails:
            body = "Subject: {}\n\n{}".format(subject,contant)
            server.sendmail('demopython4311@gmail.com',email,body)
        server.quit()
        print("Mail send successfully")
        #semail = request.POST.get('from_email')
        print(sub,msg,email)
        return render(request, 'Single_Email/Finished.html')
    return render(request, 'Single_Email/index.html')

def test(request):
    if request.method=="POST":
        file = request.POST.get("file")
        print(file)
        '''e = pd.read_excel(file)
        emails = e['Emails'].values
        for email in emails:
            print(email)'''
        return render(request, 'Single_Email/Finished.html')
    return render(request, 'Single_Email/test.html')
