import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Posta


class Command(BaseCommand):
    help = 'Load data from EV Station file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'Posta.csv'
        keys = ('dénomination du bureau de poste', 'LONGITUDE', 'LATITUDE')  # Update for correct columns

        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names
                longitude = row.get('LONGITUDE')
                latitude = row.get('LATITUDE')
          
                if longitude and latitude:  # Check for missing values
                    record = {
                      #  'code': row['code comptable'],
                        'longitude': float(longitude),
                        'latitude': float(latitude),
                        'dénomination':row['dénomination du bureau de poste'],
                        
                        'commune':row['COMMUNE'],
                        'Classe':row['Classe'],
                    }
                    records.append(record)

        # Add valid records to the database
        for record in records:
            Posta.objects.get_or_create(**record)

        