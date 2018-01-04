from django.conf.urls import url

from .views import PostListView,PostDetailView,PostDetailSlugView,post_list_view


urlpatterns = [
    
    #url(r'^$',PostListView.as_view(),name='blog'),
    url(r'^$',post_list_view,name='blog'),
    #url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(),name='post_detail'),
    url(r'^(?P<slug>[\w-]+)/$',PostDetailSlugView.as_view(),name="detail"),
]
