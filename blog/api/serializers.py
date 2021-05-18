from rest_framework import serializers
from blog.models import Post ,Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image' , 'short_description' ,'cretated_at' , 'update_by' , )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('name' , 'create_at' , 'email' , 'comments')