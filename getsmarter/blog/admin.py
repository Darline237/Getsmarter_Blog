from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "content", "create_at", "status")
    list_filter = ("status",)
    search_fields = ("title",)
admin.site.register (Article, ArticleAdmin)


# Register your models here.
