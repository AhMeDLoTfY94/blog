from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator


class PostQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class PublishedManager(models.Manager):
	def get_queryset(self):
		return PostQuerySet(self.model,using=self._db)

	def all(self):
		return self.get_queryset().active()
	def active(self):
		return self.get_queryset().active()

	def get_by_id(self,id):
		qs =self.get_queryset().filter(id=id)
		if qs.count()==1:
			return qs.first()
		return None






class Post(models.Model):
	title  = models.CharField(max_length=250)
	slug   = models.SlugField(max_length=250, unique=True,blank=True)
	author = models.ForeignKey(User, related_name='blog_Posts')
	body   = models.TextField()
	publish= models.DateTimeField(default=timezone.now)
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	objects = models.Manager()
	published = PublishedManager()


	class Meta:
		ordering =('-publish',)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/{slug}'.format(slug=self.slug)
		
def Post_pre_save_reciver(sender,post,*args,**kwargs):
    if not post.slug:
        post.slug=unique_slug_generator(post)
pre_save.connect(Post_pre_save_reciver,sender=Post)

