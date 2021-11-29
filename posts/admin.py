from django.contrib import admin
from .models import Post
from .models import Post, Date

admin.site.register(Post)
admin.site.register(Date)
