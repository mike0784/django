from django.core.management.base import BaseCommand
from mybd.models import Product

class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        obj = Product.objects.all()
        self.stdout.write(f'{obj}')