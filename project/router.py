from accounts.api.viewsets import ProfileViewSet , CommentViewSet ,AppointmentViewSet
from blog.api.viewsets import PostViewSet ,CommentViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('profile' , ProfileViewSet)
router.register('comment' , CommentViewSet)
router.register('appointment' , AppointmentViewSet)
router.register('blog' , PostViewSet)
router.register('commentpost' , CommentViewSet)
