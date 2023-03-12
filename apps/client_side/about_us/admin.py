from django.contrib import admin

from apps.client_side.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass
    # list_display = (
    #     "id",
    #     "content",
    #     "image",
    #     "created_at",
    # )

