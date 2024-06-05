import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Algerie_Telecom  # Assuming 'Ooredoo' model for new data

class Command(BaseCommand):
    help = 'Load data from Algerie_Telecom data file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / '4G_1.csv'  # Adjust file path
        #keys = ('adresse_site', 'LONGITUDE', 'LATITUDE')  # Update for correct columns

        records = []
        with open(data_file, 'r')as csvfile:  # Specify encoding for potential non-ASCII characters
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names
                longitude = row.get('LONGITUDE')
                latitude = row.get('LATITUDE')

                if longitude and latitude:  # Check for missing values

                    record = {
                            'adresse_site': row['adresse site'],
                            'longitude': float(longitude),
                            'latitude': float(latitude),
                            'commune': row['commune'],
                            "type":row["TYPE d'equipement d'acces (LTE)"],

                        }
                    records.append(record)

        # Add valid records to the database (avoid duplicates using get_or_create)
        for record in records:
            Algerie_Telecom.objects.get_or_create(**record)
