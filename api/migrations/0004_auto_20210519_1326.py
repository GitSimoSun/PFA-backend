# Generated by Django 3.2.3 on 2021-05-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210518_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
