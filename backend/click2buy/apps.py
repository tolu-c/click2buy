from django.apps import AppConfig


class Click2BuyConfig(AppConfig):
    name = 'click2buy'
    
    def ready(self):
        import click2buy.signals

