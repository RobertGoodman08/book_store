from django.contrib import admin

from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_display_links = ('user',)



admin.site.register(Comment, CommentAdmin)