from django.shortcuts import render,HttpResponse,redirect
from register.models import account

def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')

def registration(request):
    if (account.objects.filter(email=request.POST['email']).exists()):
        return render(request
        ,'failure_register.html')
        
    user = account.objects.create(uname=request.POST['uname'], email=request.POST['email'] , password=request.POST['password'])
    user.save()
    # request.session['id'] = user.id
    # return redirect('/register/login')
    # return render(request,'login.html')
    return render(request,'success_register.html')
    
def login(request):
    if (account.objects.filter(email=request.POST['login_email']).exists()):
        user = account.objects.filter(email=request.POST['login_email'])[0]
        if (request.POST['login_password']==user.password):
            # request.session['id'] = user.id
            # return redirect('/success')
            return render(request,'success.html')
    return render(request,'failure_login.html')


# def success(request):
#     user = account.objects.get(id=request.session['id'])
#     context = {
#         "user": user
#     }
#     return render(request, 'register/success1.html', context)
