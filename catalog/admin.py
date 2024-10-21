from django.contrib import admin

from catalog.models import Product, Category, Version
from myblog.models import Myblog
from sending.models import Client, Mailing


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Myblog)
class MyblogAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "fio", "comment")


@admin.register(Mailing)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "date_time", "periodicity", "status")
