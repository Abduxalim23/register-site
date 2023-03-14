from django.shortcuts import render
from .models import Registration
# Create your views here.
def post_register(request):
    if request.POST:
        reg = Registration()
        reg.first_name = request.POST['first_name']
        reg.last_name = request.POST['last_name']
        reg.company = request.POST['company']
        reg.email = request.POST['email']
        reg.phone_number = request.POST['area_code'] + request.POST['phone']
        reg.subject = request.POST['subject']
        reg.save()
    return render(request, 'index.html')
