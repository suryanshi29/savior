from django.template import loader
from django.urls import reverse
from urllib import request

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import formInfo, loginfrom


# from .models import EmergencyContact

def home(request):
    return render(request,"home.html")
def hospital(request):
    return render(request,"hospital.html")

def emergencyfrom(request):
    return render(request,"emergencyfrom.html")
def hospage(request):
    return render(request,"hospage.html")
def hospital_list(request):
    return render(request,"hospital_list.html")
def patient(request):
    return render(request,"patient.html")
def test(request):
    if request.method=="POST":
        obj=formInfo()
        obj.name=request.POST.get('name')
        obj.password=request.POST.get('password')
        obj.image=request.FILES.get('image')
        obj.save()
        return HttpResponse(request,"data submitted successfully")
    return render(request,'test.html')


def login(request):
    if request.method=="POST":
        name=request.POST('username')
        password=request.POST('password')
        data=login.objects.get(id=1)
        uname=data.name
        upassword=data.password
        if uname==name and upassword==password:
            data1=login.objects.all()
            return render(request,)





def display(request):

    data1=formInfo.objects.all()
    return render(request,'display.html',{"key1":data1})
def delete(request,id):
    data2=formInfo.objects.get(id=id)
    data2.delete()
    return HttpResponseRedirect(reverse(display))
def update(request,id):
    data=formInfo.objects.get(id=id)
    template=loader.get_template('update.html')
    testing={"update_data":data}
    return HttpResponse(template.render(testing,request))

def updaterecord(request,id):
    fname=request.POST["name"]
    fpassword=request.POST["password"]
    obj=formInfo.objects.get(id=id)
    obj.name=fname
    obj.password=fpassword
    obj.save()
    return HttpResponseRedirect(reverse('display'))








# def emergencyfrom(request):
#    if request.method=="POST":
#        obj=EmergencyContact()
#        obj.location=request.POST.get('location')
#        obj.hospital = request.POST.get('hospital')
#        obj.patient_name = request.POST.get('patient_name')
#        obj.age = request.POST.get('age')
#        obj.emergency = request.POST.get('emergency')
#        obj.gender = request.POST.get('gender')
#        obj.contact_name = request.POST.get('contact_name')
#        obj.relationship = request.POST.get('relationship')
#        obj.phone_number = request.POST.get('phone_number')
#        obj.email = request.POST.get('email')
#        obj.home_address = request.POST.get('home_address')
#        obj.ambulance_service = request.POST.get('ambulance_service')
#        obj.pickup_address = request.POST.get('pickup_address')
#
#        obj.save()
#        return  render(request,'emergencyfrom.html')
#    else:
#        return render(request,'home.html')


