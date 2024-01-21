from django.core.management.base import BaseCommand
from mybd.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(surname = 'Костромин',
        name = 'Василий',
        patronymic = 'Петрович',
        email = 'kvasia@gmail.com',
        telephone = '+79278889921',
        country = 'Росия',
        region = 'Республика Марий Эл',
        destrict = 'Волжский район',
        city = 'Волжск',
        street = 'Советская',
        home = '33',
        liter = '',
        flat = '43')
        user.save()
        self.stdout.write(f'{user}')