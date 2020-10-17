from django.contrib import admin
from ads.models import Ad, Comment

# Register your models here.

class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
