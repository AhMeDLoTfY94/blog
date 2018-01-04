from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView,DetailView

from .models import Post




class PostListView(ListView):
	template_name ="index.html"
	

	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Post.objects.all()

    
def post_list_view(request):
	queryset = Post.objects.all()
	paginator= Paginator(queryset, 3)
	page = request.GET.get("page")
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context ={
	'page':page,
	'posts':posts
	}
	return render(request,"index.html",context)



class PostDetailView(DetailView):
	template_name ="post/detail.html"

	def get_context_data(self,*args,**kwargs):
		context=super(PostDetailView,self).get_context_data(*args,**kwargs)
		return context

	def get_object(self,*args,**kwargs):
		request=self.request
		pk =self.kwargs.get('pk')
		post=Post.objects.get_by_id(pk)
		if post is None:
			raise Http404("Post doesnt exist")
		return post





def post_detail_view(request,pk=None,*args,**kwargs):
	post=Post.objects.get_by_id(pk)
	if post in None:
		raise Http404("Post dosent exist")
     

	context ={
	'post':post

	}
	return render(request,"post/detail.html",context)


class PostDetailSlugView(DetailView):
	post = Post.objects.all()
	template_name="post/detail.html"

	def get_object(self,*args,**kwargs):
		request =self.request
		slug = self.kwargs.get('slug')
		try:
			post=get_object_or_404(Post,slug=slug,active=True)
		except Post.DoesNotExist:
			raise("Not Found..")
		except Post.MultipleObjectsReturned:
			qs = Post.objects.filter(slug=slug,active=True)
			post = qs.first()
		except:
			raise Http404("No Page For you")
		return post
			

			

		
        