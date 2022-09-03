from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)

def __str__(self):
    return self.title