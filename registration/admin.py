from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .models import RegistrationProfile, Profile
from .users import UsernameField
from .utils import _


class RegistrationAdmin(admin.ModelAdmin):
    actions = ["activate_users", "resend_activation_email"]
    list_display = ("user", "activation_key_expired")
    raw_id_fields = ["user"]
    search_fields = (
        "user__{0}".format(UsernameField()),
        "user__first_name",
        "user__last_name",
    )

    def activate_users(self, request, queryset):
        """
        Activates the selected users, if they are not already
        activated.

        """

        site = get_current_site(request)
        for profile in queryset:
            RegistrationProfile.objects.activate_user(
                profile.activation_key, site
            )

    activate_users.short_description = _("Activate users")

    def resend_activation_email(self, request, queryset):
        """
        Re-sends activation emails for the selected users.

        Note that this will *only* send activation emails for users
        who are eligible to activate; emails will not be sent to users
        whose activation keys have expired or who have already
        activated.

        """

        site = get_current_site(request)
        for profile in queryset:
            user = profile.user
            RegistrationProfile.objects.resend_activation_mail(
                user.email, site, request
            )

    resend_activation_email.short_description = _("Re-send activation emails")


User = get_user_model()
admin.site.register(RegistrationProfile, RegistrationAdmin)
admin.site.register(User)
admin.site.register(Profile)
