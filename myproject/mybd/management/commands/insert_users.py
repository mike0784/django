from django.core.management.base import BaseCommand
from mybd.models import User
import csv

class Command(BaseCommand):
    help = "Create user."

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
                    user = User(surname = row[0],
                    name = row[1],
                    patronymic = row[2],
                    email = row[3],
                    telephone = row[4],
                    country = row[5],
                    region = row[6],
                    destrict = row[7],
                    city = row[8],
                    street = row[9],
                    home = row[10],
                    liter = row[11],
                    flat = row[12])
                    user.save()
                count += 1
        self.stdout.write(f'Всего в файле {count} строк.')