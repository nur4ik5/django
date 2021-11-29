from django.contrib import admin
from .models import Post
from .models import Post, Adversement

admin.site.register(Post)
admin.site.register(Adversement)
