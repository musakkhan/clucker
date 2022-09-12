from django.contrib import admin
from microblogs.models import Post, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active'
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  [
        'author','text','created_at'
    ]
