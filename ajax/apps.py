from django.apps import AppConfig


class AjaxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ajax'
    def ready(self):
        import ajax.signals