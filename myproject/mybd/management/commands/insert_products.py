from django.core.management.base import BaseCommand
from mybd.models import Product
import csv

class Command(BaseCommand):
    help = "Create products."

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
                self.stdout.write(f'{row}')
                if count == 0:
                    count += 1
                    continue
                else:
                    product = Product(name = row[0],
                                   description = row[1],
                                   price = row[2],
                                   quantity = row[3])
                    product.save()
                count += 1
        self.stdout.write(f'Всего в файле {count} строк.')