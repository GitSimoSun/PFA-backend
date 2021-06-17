# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'category'


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    top_tools = models.TextField(blank=True, null=True)
    tools = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'company'

class ParentCategory(models.Model):
    name = models.TextField(blank=True, null=True)
    parent = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'parent_category'


class Tool(models.Model):
    name = models.TextField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    stacks_num = models.IntegerField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tool'


