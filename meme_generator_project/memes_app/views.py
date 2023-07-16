from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import User_login, User_signup
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import MemeImages
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
import base64
 


# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_signup(request):

    if request.method == 'POST':
        signupform = User_signup(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request, 'Account create successfully ✅')
            return redirect('signin')
    else:
        signupform = User_signup()

    context = {'signupform': signupform}
    return render(request, 'usersignup.html', context)


def user_login(request):

    if request.method == 'POST':
        loginform = User_login(request, request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.success(request, 'Loged in ✅')
                return redirect('editor')

        return render(request, 'userlogin.html', {'loginform': loginform})

    else:
        loginform = User_login
        return render(request, 'userlogin.html', {'loginform': loginform})


def user_logout(request):
    logout(request)
    return redirect('index')


def editor_home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            image_data = request.POST.get('imageData')
            image_data = image_data.split(';base64,')[1]
            decoded_image = base64.b64decode(image_data)

            if decoded_image:
                edimg = MemeImages(uid=User.objects.get(username=request.user))
                edimg.memeImage.save(
                    'meme_image.png', ContentFile(decoded_image), save=True)

                return HttpResponseRedirect('/meme-download-page/')
            else:
                pass
        return render(request, 'editorpage.html')
    else:
        return HttpResponseRedirect('/signin/')


@login_required(redirect_field_name="/signin/")
def meme_download(request):

    all_meme = MemeImages.objects.filter(
        uid=User.objects.get(username=request.user))

    context = {'allimage': all_meme}

    return render(request, 'downloads.html', context)


@login_required(redirect_field_name="/signin/")
def del_meme(request, pk):
    delimg = MemeImages.objects.get(id=pk)
    delimg.delete()
    return HttpResponseRedirect('/meme-download-page/')
