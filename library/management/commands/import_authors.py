import csv
from django.core.management.base import BaseCommand
from library.models import Author
from datetime import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    try:
                        birth_date = self.create_date_from_year(row.get('birth_date'))
                        death_date = self.create_date_from_year(row.get('death_date'))
                        
                        Author.objects.create(
                            name=row['name'],
                            birth_date=birth_date,
                            birth_place=row.get('birth_place', ''),
                            country=row.get('country', ''),
                            death_date=death_date,
                            death_place=row.get('death_place', '')
                        )
                    except Exception as e:
                        print(self.style.WARNING(f'Error: {e}, {row} skipped.'))
                print(self.style.SUCCESS(f'{file_path} imported successfully.'))
        except FileNotFoundError:
            print(self.style.ERROR(f'{file_path} does not exist.'))

    def create_date_from_year(self, date_str):
        if date_str:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print(self.style.WARNING(f'Invalid date format: {date_str}'))
                return None
        return None