from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from .models import Email
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import redirect

# Create your views here.
def index(request):
    job=Job.objects.all()[:10]
    paginator=Paginator(job,4)
    page=request.GET.get('page')
    #?page=2
    job=paginator.get_page(page)
    #return HttpResponse("hello")
    context={
    'job':job,
    }
    return render(request,"index.html",context)

def post(request):
    
     #return HttpResponse("hello from signup")
    return render(request,"post.html")

def summary(request,id):
    job=Job.objects.get(id=id)
    context={
    'job':job,
    }
    return render(request,"summary.html",context)
def search(request):
    
    template='index.html'
    query=request.GET.get('q')
    if query:
        job=Job.objects.all()[:10]
        results=Job.objects.filter(Q(title__icontains = query) | Q(location__icontains = query) | Q(company__icontains= query))
        context={
        'job':results,
         }

        return render(request,template,context)
    else:
        return HttpResponse("Please enter a search term")

def gpa(request):
    template="index.html"
    query="gpa"
    if query:
        job=Job.objects.all()[:10]
        results=Job.objects.filter(summary__icontains = "gpa")
        context={
        'job':results,
        }
        return render(request,template,context)
        
    else:
        return HttpResponse("Please enter a search term")

def nogpa(request):
    template="index.html"
    query="gpa"
    job=Job.objects.all()
    results=Job.objects.exclude(summary__icontains="gpa")
    context={
    'job':results,
    }
    return render(request,template,context)
def contact(request):
    template="contact.html"
    return render(request,template)



def donate(request):
    template="donate.html"
    return render(request,template)

def addemail(request):
    if(request.method == 'POST'):
        email=request.POST['email']
        emailobj=Email(email=email)
        emailobj.save();

        return redirect('/')

    else:
        return render(request,'index.html')
            











