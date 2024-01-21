from django.core.management.base import BaseCommand
from mybd.models import Product

class Command(BaseCommand):
    help = "Update product name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        obj = Product.objects.filter(pk=pk).first()
        if name != '*':
            obj.name = name
        if description != '*':
            obj.description = description
        if price != 0:
            obj.price = price
        if quantity != -1:
            obj.quantity = quantity
        obj.save()
        self.stdout.write(f'{obj}')