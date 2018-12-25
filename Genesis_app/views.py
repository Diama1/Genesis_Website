from django.shortcuts import render
from Genesis_app.models import *


# Create your views here.
home = Home.objects.all()
about_msg = About_message.objects.all()
values = Core_value.objects.all()
expertise = Expertise.objects.all()
team = Team.objects.all()
contact_info = Contact_info.objects.all()

context = {'home':home,'about_msg':about_msg,'values':values,'expertise':expertise,'team':team,'contact_info':contact_info}

def index(request):

    return render(request, 'index.html', context)
