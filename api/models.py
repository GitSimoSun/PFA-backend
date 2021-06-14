# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    top_tools = models.TextField(blank=True, null=True)
    tools = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'company'

class ParentCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    parent = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'parent_category'

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'category'

class Tool(models.Model):
    name = models.CharField(max_length=100, null=True)
    category_id = models.IntegerField(null=True)
    stacks_num = models.IntegerField(null=True)
    logo = models.TextField(null=True)

    class Meta:
        db_table = 'tool'


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=255, null=False)
    matched_companies = models.TextField(null=True)
    tools_using = models.TextField(null=True)

    class Meta:
        db_table = 'user'


