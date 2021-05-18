from django import forms
from .models import Post ,  Comment
from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    content = forms.CharField( widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title' , 'image' , 'content' , 'short_description'  ]

class PostUpdateForm(forms.ModelForm):
    content = forms.CharField( widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title' , 'image' , 'content' , 'short_description'  ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post' , 'name' , 'email' , 'comments')