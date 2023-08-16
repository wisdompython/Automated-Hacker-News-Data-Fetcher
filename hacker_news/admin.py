from django.contrib import admin

from. models import Items, Comments

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id','title','descendants','type')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent',  'item')

# Register your models here.
