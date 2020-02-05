from django.shortcuts import render
from tba_app.models import registration,admin,contact
from datetime import date,timedelta,datetime
from django.http import HttpResponse
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        emailid=request.POST.get('emailid')
        types=request.POST.get('types')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        joiningdate=request.POST.get('joiningdate')
        duration=request.POST.get('duration')
        password=request.POST.get('password')
        a=registration(name=name,mobileno=mobileno,emailid=emailid,types=types,officeadd=officeadd,residenceadd=residenceadd,joiningdate=joiningdate,duration=duration,status='pending',password=password)   
        a.save()
        return render(request,'reg.html')
def viewreg(request):
    quryset=registration.objects.all()
    return render(reqeuest,'adminhome.html',{'authors':queryset}) 
def viewaproving(request):
    queryset=registration.objects.all().filter(status='pending')
    return render(request,'aprovingreg.html',{'authors':queryset})     
def viewpublic(request):
    queryset=registration.objects.all().filter(status='Approved')
    return render(request,'member.html',{'authors':queryset})     
def approve(request):
    if request.method=='POST':
        id=request.POST.get('id')
        q=registration.objects.all().filter(id=id)[0]
        dur=q.duration
        join=q.joiningdate
        if dur=='3 Months':
            dd=90
        elif dur=='6 Months':
            dd=180
        elif dur=='1 Year':
            dd=365
        elif dur=='5 Year':
            dd=1825  
        d=timedelta(dd)
        exp=join+d              
        today = str(date.today())
        registration.objects.filter(id=id).update(status='Approved',approvedate=today,expirydate=exp) 
        return viewaproving(request)   
def authentication(request):
    if request.method=='POST':
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        emailid=str(emailid)
        password=str(password)
        u=registration.objects.filter(emailid=emailid,password=password,status='Approved') 
        request.session['emailid']=emailid

        if u.count()==1:
            return render(request,'lawyerhome.html')
        else:
            v=admin.objects.filter(emailid=emailid,password=password)
            if v.count()==1:
                return render(request,'adminhome.html')
            else:
                HttpResponse('admin logined failed')
def contacts(request):
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        b=contact(name=name,email=email,subject=subject,message=message,status='off')
        b.save()
        return render(request,'index.html')
def viewcontact(request):
    queryset=contact.objects.all().filter(status="off")
    return render(request,'cont.html',{'authors':queryset}) 
def on(request):
    if request.method=='POST':
        id=request.POST.get('id')
        contact.objects.filter(id=id).update(status='ON') 
        return viewcontact(request)  
def viewprofile(request):
    queryset=registration.objects.all().filter(emailid=request.session['emailid'])
    return render(request,'profileview.html',{'authors':queryset})    
def editviewprofile(request):
    queryset=registration.objects.all().filter(emailid=request.session['emailid'])
    return render(request,'editprofile.html',{'authors':queryset})    
def edit(request):
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        emailid=request.POST.get('emailid')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        password=request.POST.get('password')
        registration.objects.filter(id=id).update(name=name,mobileno=mobileno,emailid=emailid,officeadd=officeadd,residenceadd=residenceadd,password=password) 
        return render(request,'profileview.html')                        
# Create your views here.
