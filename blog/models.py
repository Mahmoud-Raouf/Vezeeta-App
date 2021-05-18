from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify 
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    author      = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    title       = models.CharField(_("العنوان"), max_length=100)
    image       = models.ImageField(_("الصوره :"), upload_to='image', blank=True, null=True  )
    short_description = models.CharField(_("عنوان مصغر "), max_length=250)
    content     = RichTextField(_("المحتوى :"))
    cretated_at = models.DateTimeField( auto_now_add=True ,blank=True, null=True)
    update_by   = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    like                = models.ManyToManyField(User , blank=True , related_name='doc_likes')
    readed           = models.ManyToManyField(User , blank=True , related_name='doc_readed')
    slug              = models.SlugField(_("Slug :"), blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail' , args={self.slug})

    def get_like_url(self):
        return reverse("blog:likes", kwargs={"slug": self.slug})
    
    def get_readed_url(self):
        return reverse("blog:readed", kwargs={"slug": self.slug})

        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    

class Comment(models.Model):
    post = models.ForeignKey('Post', verbose_name=_("comment"), on_delete=models.CASCADE , blank=True, null=True)
    comment_author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم"), max_length=50)
    create_at = models.DateTimeField(_("أنشاء فى :"),auto_now_add=True , blank=True, null=True)
    email = models.EmailField(_("الإيميل"), max_length=50)
    comments = models.TextField(_("التعليق") , max_length=250)

    def __str__(self):
        return '{} علق على {} '.format(self.name , self.comments)

    class Meta:
        ordering = ('-create_at',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
