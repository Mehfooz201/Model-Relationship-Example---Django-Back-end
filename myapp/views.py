import email
from django.shortcuts import render
from .models import Post, Page, Song, User

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='graphicx.mehfooz201@gmail.com')
    data3 = User.objects.filter(page__page_cat='python')
    data4 = User.objects.filter(post__post_pub_date='2022-09-27')
    data5 = User.objects.filter(song__song_duration='5')

    return render(request, 'myapp/user.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})

def page(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(user__email='graphicx.mehfooz201@gmail.com')
    data3 = Page.objects.filter(page_cat='python')

    return render(request, 'myapp/page.html', {'data1':data1, 'data2':data2, 'data3':data3})

def post(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_pub_date='2022-09-27')
    data3 = Post.objects.filter(user__username='mehfooz201')

    return render(request, 'myapp/post.html', {'data1':data1, 'data2':data2, 'data3':data3})


def song(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration=5)
    data3 = Song.objects.filter(user__username='mehfooz201')

    return render(request, 'myapp/song.html', {'data1':data1, 'data2':data2, 'data3':data3})
