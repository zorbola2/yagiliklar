from django.shortcuts import render, redirect
from .models import Category, News
from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_page(request):
    if request.method == 'POST': # POST, GET, UPDATE
        savol = request.POST.get('qidiruv')
        yangiliklar = News.objects.filter(nomi__contains=savol)
        # icontains, contains
    else:
        yangiliklar = News.objects.all()
    kategoriyalar = Category.objects.all()
    
    context = {
        'kategoriyalar': kategoriyalar,
        'yangiliklar': yangiliklar
    }
    return render(request, template_name='index.html', context=context)


def category_page(request, slug):
    kategoriyalar = Category.objects.all()
    kategoriya = Category.objects.get(slug=slug)
    yangiliklar = News.objects.filter(category_id=kategoriya)
    context = {
        'kategoriyalar': kategoriyalar,
        'yangiliklar': yangiliklar
    }
    return render(request, template_name='index.html', context=context)


def single_post(request, pk):
    kategoriyalar = Category.objects.all()
    yangilik = News.objects.get(id=pk)
    context = {
        'kategoriyalar': kategoriyalar,
        'yangilik': yangilik
    }
    return render(request, template_name='singlepost.html', context=context)



def login_page(request):
    return render(request, template_name='login.html')


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            
            if password == password2:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                return redirect('login_page')
            else:
                print('Parollar bir biriga mos kelmadi')
    else:
        form = RegisterForm()
    return render(request, template_name='register.html', context={'form': form})


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)

