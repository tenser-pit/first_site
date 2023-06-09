from django.contrib import admin
from user_data.models import UserData

# Декоратор admin.register замена admin.site.register()


@admin.register(UserData)
class UserAdmin(admin.ModelAdmin):
    pass


