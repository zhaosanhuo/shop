from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#from goods.models import User
from goods.forms import UserForm

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            email = (request.POST.get('email')).strip()
            user_list = User.objects.filter(username=username)
            if user_list:
                return render(request, "goods/register.html", {'uf': uf, "error": "用户名已经存在!"})
            else:
                user = User()
                user.username = username
                user.password = password
                uese.email = email
                user.save()
                uf = LoginForm()
                return  render(request, 'goods/index.html', {'uf': uf})
    else:
        uf = UserForm()
    return render(request, "goods/register.html", {'uf': uf})
