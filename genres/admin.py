from django.contrib import admin
from genres.models import Genres


class GenresAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')


admin.site.register(Genres, GenresAdmin)
