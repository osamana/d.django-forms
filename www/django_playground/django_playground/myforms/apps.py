from __future__ import unicode_literals

from django.apps import AppConfig


class MyFormsConfig(AppConfig):
    name = 'django_playground.myforms'
    verbose_name = "MyForms"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

