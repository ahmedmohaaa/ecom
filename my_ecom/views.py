from django.shortcuts import render,get_object_or_404,redirect
from .models import Box ,Category,Catcloth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def man(request):
    context={
        'boxes':Box.objects.all(),
        'cats':Catcloth.objects.all(),
    }
    return render(request,'man.html',context)


def woman(request):
    context={
        'boxes':Box.objects.all(),
        'cats':Catcloth.objects.all(),
    }
    return render(request,'woman.html',context)


def child(request):
    context={
        'boxes':Box.objects.all(),
        'cats':Catcloth.objects.all(),
    }
    return render(request,'child.html',context)


def about(request,id):
    box = get_object_or_404(Box, id=id)
    cat = box.category


    context={
        'cat':cat,
        'boxes':box,
        'cats':Catcloth.objects.all(),
    }
    return render(request,'about.html',context)



def log(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"eror in your log in")
            return redirect('log')  

 
    return render(request,'log.html')


def home(request):
    return render(request,'home.html')




def push(request,id):
    box = get_object_or_404(Box, id=id)
    context = {
        'box':box
     
    }
    return render(request, 'push.html', context)





def payaple(request):
    if request.method == 'POST':
        # استقبل بيانات الدفع
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card = request.POST.get('card')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')

        # ممكن هنا تعمل تحقق بسيط لو عاوز
        if card and cvv and len(card) == 19 and len(cvv) == 3:
            # معناه الدفع ناجح في النظام الوهمي
            return redirect('payment_success')
        else:
            return render(request, 'payaple.html', {'error': 'Invalid card details'})

    return render(request, 'payaple.html')

def payment_success(request):
    return render(request, 'payment_success.html')