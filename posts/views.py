from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, All_list


def index(request):
	return render (request, "posts/index.html")

def user_list(request):
	return render(request,'posts/user_list.html')

def message(request):
	return render (request, "posts/message.html")

def login(request):
	return render (request, "posts/login.html")

def posts_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts 
	}
	return render (request, "posts/posts_list.html", context)

def all_list(request):
	atribut = All_list.objects.all()
	context = {
		'atribut': atribut
	}
	return render (request, "posts/all_list.html", context)

