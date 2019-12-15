from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bamcis.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import bamcis.users.signals  # noqa F401
        except ImportError:
            pass
