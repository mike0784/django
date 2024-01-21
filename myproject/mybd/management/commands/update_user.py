from django.core.management.base import BaseCommand
from mybd.models import User

class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('surname', type=str, help='User name')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('patronymic', type=str, help='User name')
        parser.add_argument('email', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        surname = kwargs.get('surname')
        name = kwargs.get('name')
        patronymic = kwargs.get('patronymic')
        email = kwargs.get('email')
        user = User.objects.filter(pk=pk).first()
        user.surname = surname
        user.name = name
        user.patronymic = patronymic
        user.email = email
        user.save()
        self.stdout.write(f'{user}')