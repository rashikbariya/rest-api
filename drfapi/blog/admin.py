from django.contrib import admin
from .forms import PostsForm
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ['owner','__str__','image']
    form = PostsForm
    # class Meta:
    #     model = Posts

admin.site.register(Posts,PostsAdmin)
