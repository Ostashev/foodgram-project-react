import csv
import logging

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.import_ingredients()
        logging.info('Загрузка ингредиентов завершена.')

    def import_ingredients(self, file='ingredients.csv'):
        logging.info(f'Загрузка {file}...')
        file_path = f'../data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
