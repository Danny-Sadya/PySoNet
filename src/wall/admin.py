from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts"""

    list_display = ("user", "moderation", "create_date", "view_count", "published", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Comments to a posts"""

    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    # actions = ["unpublish", "publish"]
    mptt_level_indent = 15