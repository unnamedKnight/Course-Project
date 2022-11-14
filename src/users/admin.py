from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdminConfig(UserAdmin):
    # model = NewUser
    search_fields = ("email",)
    list_filter = ("email", "is_active", "is_staff")
    ordering = ("-date_joined",)
    list_display = ("email", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        # (
        #     "Permissions",
        #     {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")},
        # ),
        # ("Personal info", {"fields": ("username",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        # ("Personal", {"fields": ("about",)}),
    )
    # formfield_overrides = {
    #     NewUser.about: {"widget": Textarea(attrs={"rows": 10, "cols": 40})},
    # }
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    readonly_fields = (
        "last_login",
        "date_joined",
    )


admin.site.register(User, UserAdminConfig)
