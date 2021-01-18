from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# class UserInfo(AbstractUser):
#     mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

#     class Meta:
#         db_table = 'users'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.username
    

class Issue(models.Model):
    title = models.CharField(max_length=10, verbose_name='标题')
    content = models.CharField(max_length=255, verbose_name='内容')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户ID')
    pub_at = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')


    class Meta:
        db_table = "issue"
        verbose_name = '议题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


