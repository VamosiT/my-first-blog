from django.contrib import admin
from .models import Post
from .models import URL

admin.site.register(Post)
admin.site.register(URL)