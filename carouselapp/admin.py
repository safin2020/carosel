from django.contrib import admin


from .models import Feature, CaroselModel
# Register your models here.
class FeatureAdmin(admin.ModelAdmin):

    list_display = [
        'heading',
        'slug',
        'thumbnail',
        'short_discription',
        'discription'
    ]

admin.site.register(Feature, FeatureAdmin)

class CaroselModelAdmin(admin.ModelAdmin):

    list_display = [
        'heading',
        'thumbnail',
        'short_discription'
    ]

admin.site.register(CaroselModel, CaroselModelAdmin)