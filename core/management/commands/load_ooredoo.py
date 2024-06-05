import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Ooredoo2  # Assuming 'Ooredoo' model for new data
from django.contrib.gis.geos import Point
import datetime 

class Command(BaseCommand):
    help = "Load data from Ooredoo data file"
        
    def _convert_date(self,date_str):
        date_str_list = date_str.split("/")
        return f"{date_str_list[2]}-{date_str_list[1]}-{date_str_list[0]}"

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / "data" / "wta.csv"  # Adjust file path

        records = []
        with open(
            data_file, "r"
        ) as csvfile:  # Specify encoding for potential non-ASCII characters
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names
                commune = row.get("Commune")
                longitude = row.get("LONGITUDE")
                latitude = row.get("LATITUDE")
                code_site = row.get("Code Site")
                type = row.get("Type")
                adresse = row.get("Adresse")
                wilaya = row.get("Wilaya")
                mise_en_service = row.get("Mise en service")

                record = {
                    "commune": commune,
                    #"location": Point(float(latitude),float(longitude)),
                    "longitude": float(longitude),
                    "latitude": float(latitude),
                    "code_site": code_site,
                    "type": type,
                    "adresse": adresse,
                    "wilaya": wilaya,
                    "mise_en_service": self._convert_date(mise_en_service),
                }
                records.append(record)

        for record in records:
            print(record)
            Ooredoo2.objects.get_or_create(**record)