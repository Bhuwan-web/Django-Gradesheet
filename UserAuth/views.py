from django.http.response import HttpResponse
from django.shortcuts import render

from UserAuth.forms import LoginForm, MyForm
from UserAuth.models import Login

def login(request):
    if request.method.lower()=="post":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("OKok")
        else:
            return HttpResponse("Something went Wrong")
    else:
        form=LoginForm()
        context={
            "title":"Login Form",
            "header":"Login",
            'form':form
        }
        return render(request,'UserAuth/login.html',context)

# def trial(request):
#     if(request.method=='POST'):
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponse("Eevrything's OK")
#         else:
#             return HttpResponse("Something again went wrong")
#     else:
#         form=LoginForm()
#         return render(request,'UserAuth/login.html',{'form':form})


