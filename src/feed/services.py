from src.wall.models import Post
from src.followers.models import Follower


def feed(user):
    posts = Post.objects.filter(user__owner__subscriber_id=1).order_by('-create_date')\
        .select_related('user').prefetch_related('comments')