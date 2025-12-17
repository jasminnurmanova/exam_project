from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from .forms import CustomUserRegisterForm
from django.views import View

class RegisterView(View):
    def get(self,request):
        form = CustomUserRegisterForm()
        return render(request,'user/regis.html',{'form':form})

    def post(self,request):
        form = CustomUserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect ('home')

        return render(request,'user/regis.html',{'form':form})

class ProfileView(View):
    def get(self,request):
        user = request.user
        return render(request,'users/profile.html',{'user':user})

