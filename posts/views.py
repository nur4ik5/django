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

# вьюха для списка постов и поиска
def posts_list(request):
	search = request.GET.get('q', '')
	if search:
		posts = Post.objects.filter(text__contains=search)
	else:
		posts = Post.objects.all()
	context = {
		'posts': posts,
		'search_word': search 
	}
	return render (request, "posts/posts_list.html", context)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {'post': post}
	return render(request, 'posts/post_detail.html', context)


def all_list(request):
	atribut = All_list.objects.all()
	context = {
		'atribut': atribut
	}
	return render (request, "posts/all_list.html", context)

