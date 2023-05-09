from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    
    subject = 'welcome to GFG world'
    message = f'Hi "amols9517@gmail.com", thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["amols9517@gmail.com", ]
    context=send_mail( subject, message, email_from, recipient_list )
    print(context)
    return render(request,'index.html',{'context':context})
