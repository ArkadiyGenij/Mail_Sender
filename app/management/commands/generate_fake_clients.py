from django.core.management import BaseCommand
from faker import Faker

from app.models import Client


class Command(BaseCommand):
    help = 'Генерирует 20 фейковых клиентов'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        Faker.seed(42)

        for i in range(20):
            # Генерируем данные
            first_name = fake.first_name()
            last_name = fake.last_name()
            middle_name = fake.middle_name()
            email = fake.unique.email()
            comment = fake.text(max_nb_chars=200)

            Client.objects.create(
                email=email,
                name=first_name,
                surname=last_name,
                patronymic=middle_name,
                comment=comment
            )

            self.stdout.write(self.style.SUCCESS(f'Создан клиент {i+1}: {email}'))

        self.stdout.write(self.style.SUCCESS('Успешно создано 20 фейковых клиентов'))