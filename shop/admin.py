from django.contrib import admin
from shop.models import Product, Category
# Register your models here.


# admin.site.register(Category)
# admin.site.register(Product)

class ProductStackInline(admin.StackedInline): # 以块的形式嵌入
    model = Product
    extra = 1

class ProductTabularInline(admin.TabularInline): # 以列表的形式嵌入
    model = Product
    extra = 1


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ProductTabularInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'thumb_image','name','on_sale', 'published_at', 'deleted', 'category','sort_order']
    ordering = ['id']
    list_per_page=10
    list_filter = ['category']
    search_fields = ['name']
    # fields = ['name', 'published_at'] 显示列表属性

    fieldsets = (
            ('基本', {'fields':['name','on_sale', 'published_at', 'deleted', 'category','image_url','decription']}),
            ('高级', {
                'fields':['view_count','comment_count'],
                'classes':('collapse',) # 设置为是否隐藏
            })


    )

admin.site.site_header = '长乐商城'
admin.site.site_title = '长乐商城后台管理'
admin.site.index_title = '欢迎使用长乐商城'
