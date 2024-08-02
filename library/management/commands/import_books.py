import csv

from django.core.management.base import CommandParser

from library.models import Book
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Input csv file')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    try:
                        Book.objects.create(
                            isbn=row['isbn'], 
                            title=row['title'], 
                            author=row['author'], 
                            year=row['year'], 
                            pages=row['pages']
                        )
                    except Exception as e:
                        print(self.style.WARNING(f'Error: {e}, {row} skipped.'))
                print(self.style.SUCCESS(f'{file_path} imported successfully.'))
        except FileNotFoundError:
            print(self.style.ERROR(f'{file_path} does not exist.'))

        