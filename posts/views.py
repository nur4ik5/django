from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Advertisement
from .forms import PostCreationForm


def index(request):
	return render (request, "posts/index.html")

def user_list(request):
	return render(request,'posts/user_list.html')

def message(request):
	return render (request, "posts/message.html")

def login(request):
	return render (request, "posts/login.html")


##################################### POSTS #########################################
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
	# запрос поста из бд по primary key
	# post = get_object_or_404(Post, id=pk)
	return render(request, 'posts/post_detail.html', context)


def post_create(request):
	print("HHTP метод", request.method)
	# Проверка метода запроса
	if request.method = 'POST':
		form = PostCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('posts_list')



	context = {
		'form': form 
	}
	return render(request, 'posts/post_create.html', context)

################################## ADV ##################################################

def advertisement(request):
	advertisement = Advertisement.objects.all()
	context = {
		'advertisement': advertisement
	}
	return render (request, "posts/advertisement.html", context)



def advertisement_delete(request, adv_id):
	advertisement = get_object_or_404(Advertisement, id=adv_id)
	advertisement.delete()
	# Advertisement.objects.get(id=adv_id).delete()
	# return redirect('advertisement')
	return HttpResponseRedirect(reverse('advertisement'))

