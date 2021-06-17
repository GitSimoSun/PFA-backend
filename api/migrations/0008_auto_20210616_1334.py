# Generated by Django 3.2.3 on 2021-06-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='parent',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='category_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='logo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='stacks_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
