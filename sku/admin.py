# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sku.models import Category,SubCategory,Product

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
