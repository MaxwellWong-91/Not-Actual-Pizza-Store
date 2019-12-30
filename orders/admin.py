from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(AddOn)
admin.site.register(SubType)
admin.site.register(Subs)
admin.site.register(PastaType)
admin.site.register(Pasta)
admin.site.register(SaladType)
admin.site.register(Salad)
admin.site.register(PlatterType)
admin.site.register(Platters)
admin.site.register(Order)