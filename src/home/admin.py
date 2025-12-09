from django.contrib import admin
from .models import Photo

# Register your models here.

@admin.register(Photo)
class PhotoModeladmin(admin.ModelAdmin):
    readonly_fields = ("user",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)