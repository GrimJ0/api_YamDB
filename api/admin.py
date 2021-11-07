from django.contrib import admin
from .models import (User,
                     Category,
                     Genre,
                     Title,
                     Review,
                     Comment
                     )


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'username',
                    'bio',
                    'email',
                    'role'
                    )

    search_fields = ('username',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')

class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'year',
                    'description',
                    'rating',
                    'category'
                    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'score',
                    'pub_date',
                    'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('review',
                    'text',
                    'author',
                    'pub_date')



admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

