import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Djezzy  # Assuming 'Djezzy' model for new data

class Command(BaseCommand):
    help = 'Load data from Djezzy data file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'ota10.csv'  # Adjust file path
       # keys = ('Adresse', 'LONGITUDE', 'LATITUDE')  # Update for correct columns

        records = []
        with open(data_file, 'r')as csvfile:  # Specify encoding for potential non-ASCII characters
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names
                longitude = row.get('LONGITUDE')
                latitude = row.get('LATITUDE')

                if longitude and latitude:  # Check for missing values
                
                    record = {
                            'Adresse': row['Adresse'],
                            'longitude': float(longitude),
                            'latitude': float(latitude),
                            'commune':row['Commune'],
                           
                            'Technologie':row['Technologie'],
                        }
                    records.append(record)

        # Add valid records to the database (avoid duplicates using get_or_create)
        for record in records:
            Djezzy.objects.get_or_create(**record)

        