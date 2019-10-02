# user : admin
# password : djangoAdmin
from django.contrib import admin

from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
