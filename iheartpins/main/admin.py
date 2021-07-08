from django.contrib import admin
from .models import Pin, PinSet, PinSetContent, Pinventory, PinventoryContent, Item, ItemImage


admin.site.register(Pin)
admin.site.register(PinSet)
admin.site.register(PinSetContent)
admin.site.register(Pinventory)
admin.site.register(PinventoryContent)
admin.site.register(Item)
admin.site.register(ItemImage)