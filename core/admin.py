# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(Item)
admin.site.register(ShoppingList)
admin.site.register(InstancedItem)

