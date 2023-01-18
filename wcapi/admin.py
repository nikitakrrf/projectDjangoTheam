from django.contrib import admin

from .models import *
# Register your models here.
admin.site.site_header = 'Админ панель тем'
admin.site.site_title = 'Админка темы'
admin.site.register(Themes)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(Widgets)
admin.site.register(Icon)
admin.site.register(Wallpapers)

