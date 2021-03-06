# Generated by Django 3.1.5 on 2021-01-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='commit_count',
            field=models.IntegerField(default=0, verbose_name='评论次数'),
        ),
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='观看次数'),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_sale',
            field=models.SmallIntegerField(choices=[(0, '补货中'), (1, '下架'), (2, '正常销售')], default=0, verbose_name='状态'),
        ),
    ]
