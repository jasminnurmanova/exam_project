from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from .forms import CustomUserRegisterForm, CustomUserUpdateForm,CustomUserChangePassForm
from django.views import View
from products.models import Product
from .models import CustomUser


class RegisterView(View):
    def get(self,request):
        form = CustomUserRegisterForm()
        products=form.products.all().order_by('-id')
        return render(request,'user/regis.html',{'form':form,'products':products})

    def post(self,request):
        form = CustomUserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect ('home')
        return render(request,'user/regis.html',{'form':form})

    def save(self,commit=True):
        user =super().save(commit=False)
        password=self.cleaned_data['password1']
        user.set_password(password)
        user.save()
        return user

class ProfileView(View):
    def get(self,request):
        user = request.user
        products=user.products.all().order_by('-id')
        comments=user.user_comments.all()
        context={'user':user,'products':products,'comments':comments}
        return render(request,'user/profile.html',context)


class LoginView(View):
    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        return render (request,'user/login.html')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

class ProfileUpdateView(View):
    def get(self,request):
        form = CustomUserUpdateForm(instance=request.user)
        return render(request,'user/profile-update.html',{'form':form})

    def post(self,request):
        user = request.user
        form = CustomUserUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect ('user:profile')

        return render(request,'user/profile-update.html',{'form':form })

class CustomUserChangePassView(View):
    def get(self,request):
        form = CustomUserChangePassForm()
        return render(request,'user/change_pass.html',{'form':form})

    def post(self,request):
        form = CustomUserChangePassForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            update_session_auth_hash(request, request.user)
            return redirect ('user:profile')

        return render(request,'user/change_pass.html',{'form':form })