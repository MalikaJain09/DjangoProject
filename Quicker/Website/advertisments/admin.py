from django.contrib import admin

from .models import Category , Products , UserAdd , RegisterAdd , Review , sub_category

admin.site.register(Category)
admin.site.register(sub_category)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(UserAdd)
admin.site.register(RegisterAdd)

