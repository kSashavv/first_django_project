from django.contrib import admin
from office.models import Application, Post, Category




class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Application)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)