import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Service_Universel  # Assuming 'localité' model for new data

class Command(BaseCommand):
    help = 'Load data from  localité data file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'np.csv'  # Adjust file path
      #  keys = ('LOCALITÉ', 'LONGITUDE', 'LATITUDE')  # Update for correct columns

        records = []
        with open(data_file, 'r', encoding='utf-8')as csvfile:  # Specify encoding for potential non-ASCII characters
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names
                longitude = row.get('Latitude')
                latitude = row.get('Longitude')
                populations=row.get('Populations')
               
                print(longitude)
                if longitude and latitude:  # Check for missing values

                    record = {
                            'localité': row['LOCALITÉ'],
                            'longitude': float(longitude),
                            'latitude': float(latitude),
                            'populations':populations,
                            'commune':row['COMMUNE'],
                            'municipality':row['البلدية'],
                            'region':row['المنطقة'],
                        }
                    records.append(record)

        # Add valid records to the database (avoid duplicates using get_or_create)
        for record in records:
            print(record)
            Service_Universel.objects.get_or_create(**record)
