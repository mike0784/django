from django.core.management.base import BaseCommand
from mybd.models import Order, User, Product
import csv

class Command(BaseCommand):
    help = "Insert new product"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='name file')
    
    def handle(self, *args, **kwargs):
        file = kwargs['file']
        with open(file, encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter = ";")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                        count += 1
                        continue
                else:
                    user_id = int(row[0])
                    if user_id == 15:
                        self.stdout.write(f'user_id = {user_id}')
                        user = User.objects.filter(id=user_id).first()
                        if not user:
                            self.stdout.write(f'Пользователь с данным id = {user_id} не найден')
                        else:
                            order = Order(customer = user, total_price = float(row[1]))
                            order.save()
                        count += 1
            self.stdout.write(f'Всего в файле {count} строк.')
        # pk1 = kwargs.get('pk')
        # user = User.objects.filter(pk=pk1).first()
        # if not user:
        #     self.stdout.write(f'Пользователь с данным id = {pk1} не найден')
        # else:
        #     pk2 = kwargs.get('id')
        #     product = Product.objects.filter(pk=pk2).first()
        #     if not product:
        #         self.stdout.write(f'Продукт с данным id = {pk2} не найден')
        #     else:
        #         total_price = product.price * kwargs.get('count')
        #         obj = Order.objects.create(customer = user, total_price = total_price)
        #         #obj.customer = user
        #         obj.products.set = product
        #         #obj.total_price = total_price
        #         self.stdout.write(f'Сумма={total_price}')
        #         #obj = Order(customer = user, products = product, total_price = total_price)
        #         obj.save()
        #         self.stdout.write(f'{obj}')