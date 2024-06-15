from django.core.management.base import BaseCommand
from fetch_trade_stream.services.ws_services import connect_ws

class Command(BaseCommand):
    help = 'Start fetching Binance trade stream'
    
    def handle(self, *args, **options):
        connect_ws()
        pass
