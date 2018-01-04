from django.contrib import admin


from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', '__str__', 'slug', 'author', 'publish', 'active')
	list_filter  = ('active', 'created', 'publish', 'author')
	search_fields= ('title', 'body')
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields =('author',)
	date_hierarchy = 'publish'
	ordering =['active','publish']
admin.site.register(Post, PostAdmin)