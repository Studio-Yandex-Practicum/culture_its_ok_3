from django.contrib import admin

from .models import Exhibit, Journey, ReviewOnExhibit, ReviewOnRoute, Route


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "rating"
    )
    search_fields = ("description", "title")
    list_filter = ("rating",)
    empty_value_display = "-пусто-"


class ExhibitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "address",
        "rating",
        "author",
        "route"
    )
    search_fields = ("description",)
    list_filter = ("name", )
    empty_value_display = "-пусто-"
    list_editable = ("route",)


class ReviewOnRouteAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "exhibit",
        "author",
        "contact",
    )
    search_fields = ("text", "exhibit",)
    list_filter = ("author", "exhibit")
    empty_value_display = "-пусто-"


class ReviewOnExhibitAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "route",
        "author",
        "contact",
    )
    search_fields = ("text", "route",)
    list_filter = ("author", "route")
    empty_value_display = "-пусто-"

from .forms import ProfileForm
from .models import Message, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('traveler', 'route', 'now_exhibit',)


admin.site.register(Route, RouteAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(ReviewOnRoute, ReviewOnExhibitAdmin)
admin.site.register(ReviewOnExhibit, ReviewOnRouteAdmin)