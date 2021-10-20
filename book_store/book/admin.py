from django.contrib import admin
from book.models import Category,Book, Subcategory,Images, Rating
from book.views import user_login
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','category']
    list_filter = ['category']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Book,BookAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Rating)