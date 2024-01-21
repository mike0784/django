from django.core.management.base import BaseCommand
from mybd.models import Order, User, Product

class Command(BaseCommand):
    help = "Insert new product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('id', type=int, help='Product ID')
        parser.add_argument('count', type=int, help='count products')
    
    def handle(self, *args, **kwargs):
        pk1 = kwargs.get('pk')
        user = User.objects.filter(pk=pk1).first()
        if not user:
            self.stdout.write(f'Пользователь с данным id = {pk1} не найден')
        else:
            pk2 = kwargs.get('id')
            product = Product.objects.filter(pk=pk2).first()
            if not product:
                self.stdout.write(f'Продукт с данным id = {pk2} не найден')
            else:
                total_price = product.price * kwargs.get('count')
                obj = Order.objects.create(customer = user, total_price = total_price)
                #obj.customer = user
                obj.products.set = product
                #obj.total_price = total_price
                self.stdout.write(f'Сумма={total_price}')
                #obj = Order(customer = user, products = product, total_price = total_price)
                obj.save()
                self.stdout.write(f'{obj}')