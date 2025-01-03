from importlib import reload

from django.test import TestCase
from django.test.utils import override_settings

from registration import forms
from registration.users import UsernameField


class RegistrationFormTests(TestCase):
    """
    Test the default registration forms.

    """

    def setUp(self):
        # The form's Meta class is created on import. We have to reload()
        # to apply the new AUTH_USER_MODEL to the Meta class.
        reload(forms)

    def test_registration_form_adds_custom_user_name_field(self):
        """
        Test that ``RegistrationForm`` adds custom username
        field and does not raise errors

        """

        form = forms.RegistrationForm()

        self.assertTrue(UsernameField() in form.fields)

    def test_registration_form_subclass_is_valid(self):
        """
        Test that ``RegistrationForm`` subclasses can save

        """
        data = {
            "username": "foo",
            "email": "foo@example.com",
            "password1": "o09o@exa.c9om3",
            "password2": "o09o@exa.c9om3",
        }

        form = forms.RegistrationForm(data=data)
        print(form.errors)

        self.assertTrue(form.is_valid())
