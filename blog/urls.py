from django.urls import path

from . import views
from .views import BlogList , BlogDetail , CreateBlogView ,UpdateBlogView , DeleteBlogView ,DocLikeRedirect
app_name = 'blog'

urlpatterns = [
    # path('' , views.blog_list , name='blog_list' ),
    # path('<slug:slug>/' , views.blog_detail , name='blog_detail' ),
    path('add-blog/' , CreateBlogView.as_view() , name='add_blog'),
    path('<slug:slug>/' , BlogDetail.as_view() , name='blog_detail' ),
    path('<slug:slug>/update/' , UpdateBlogView.as_view() , name='update_blog' ),
    path('<slug:slug>/delete/', DeleteBlogView.as_view(), name='delete_post'),
    path('' , BlogList.as_view() , name='blog_list' ),
    path('<slug:slug>/like/', views.DocLikeRedirect.as_view() , name='likes'),
    

]