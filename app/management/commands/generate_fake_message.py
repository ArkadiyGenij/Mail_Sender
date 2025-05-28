from django.core.management import BaseCommand
from faker import Faker

from app.models import Message


class Command(BaseCommand):
    help = 'Генерирует 20 фейковых сообщений'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        Faker.seed(42)

        for i in range(20):
            title = fake.name()
            message = fake.text(max_nb_chars=500)

            Message.objects.create(title=title, body=message)

            self.stdout.write(self.style.SUCCESS(f'Создано сообщение {i + 1}: {title}'))

        self.stdout.write(self.style.SUCCESS('Успешно создано 20 фейковых сообщений'))
