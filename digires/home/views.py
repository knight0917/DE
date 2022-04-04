from django.shortcuts import redirect, render 
from home.models import UserDetail


# Create your views here.

def home(request):
    return render(request, 'home.html')
   
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def template(request):

    if request.method == 'POST':
        
        nm     = request.POST.get('name')
        eml    = request.POST.get('email')
        adrs   = request.POST.get('address')
        ph     = request.POST.get('phone')
        wb     = request.POST.get('web')
        lkdn   = request.POST.get('linkedin')
        gthb   = request.POST.get('github')
        img    = request.POST.get('photo')
        acdql  = request.POST.get('acadqual')
        wrkex  = request.POST.get('workexp')
        inter  = request.POST.get('inter')
        about  = request.POST.get('about')

        data = UserDetail(name=nm, email=eml, address=adrs, phone=ph, web=wb, linkedin=lkdn, github=gthb, photo=img, acadqual=acdql, workexp=wrkex, inter=inter, about=about)
        data.save()

        return redirect('userdata/')
    else:
        return render(request, 'template.html')

def temp1(request):
    userdetail = UserDetail.objects.last()
    return render(request, 'temp1.html', {'userdetail':userdetail})
