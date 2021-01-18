from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    sort = models.IntegerField(default=0, verbose_name='排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class Product(models.Model):
    SALE_CHOICES = (

        (0, '补货中'),
        (1, '下架'),
        (2, '正常销售')
    )

    name = models.CharField(max_length=20, verbose_name='名称')
    on_sale = models.SmallIntegerField(choices=SALE_CHOICES, default=0, verbose_name='状态')
    decription = models.CharField(max_length=200,null=True, verbose_name='描述信息')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    deleted = models.BooleanField(default=False, verbose_name='软删除')
    published_at = models.DateField(verbose_name='发布日期')
    view_count = models.IntegerField(default=0, verbose_name='观看次数')
    comment_count = models.IntegerField(default=0, verbose_name='评论次数')
    image_url = models.ImageField(upload_to='product/%Y-%m-%d', verbose_name='图片', null=True) 


    class Meta:
        # db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


    def sort_order(self):
        return self.category.id

    
    # def thumb_image(self):
    #     if not self.image_url:
    #         return '无图片'
    #     else:
    #         return mark_safe('<img src="/static/uploads/%s" style="height:60px; border-radius: 5px;">' % (self.image_url))

    sort_order.short_description = '分类顺序'
    sort_order.admin_order_field = 'category'

    def thumb_image(self):
        if not self.image_url:
            return '无图片'
        else:
            return mark_safe('<img src="/static/uploads/%s" style="height: 45px; border-radius: 5px;">' % (self.image_url))

    thumb_image.short_description = '缩略图'
    # thumb_image.admin_order_field = 'image_url' 图片排序


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )