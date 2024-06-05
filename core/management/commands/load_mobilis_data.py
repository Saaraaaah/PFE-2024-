import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Mobilis  # Assuming 'Mobiliss' model for new data
import datetime

class Command(BaseCommand):
    help = "Load data from Mobilis data file"

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / "data" / "atm.csv"  # Adjust file path

        records = []
        with open(
            data_file, "r"
        ) as csvfile:  # Specify encoding for potential non-ASCII characters
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Use the correct column names

                Nom_du_Site= row.get("Nom du Site")
                latitude = row.get("LATITUDE")
                longitude = row.get("LONGITUDE")
                Code_Site = row.get("Code Site")
                Type = row.get("Type")
                Typologie = row.get("Typologie")
                T_Salle_Equip = row.get("T. Salle Equip.")             
                Type_Gardiennage = row.get("Type Gardiennage")
                Commune = row.get("Commune")
                Etat = row.get("Etat")
                D_Mise_en_Air = row.get("D. Mise en Air")
                Propriétaire = row.get("Propriétaire")

                if not D_Mise_en_Air:
                    D_Mise_en_Air = None
                    
                record = {
                    "Nom_du_Site": Nom_du_Site,
                    "longitude": float(longitude) if longitude else None,
                    "latitude": float(latitude) if latitude else None,
                    "Code_Site": Code_Site,
                    "Type": Type,
                    "Typologie": Typologie,
                    "T_Salle_Equip": T_Salle_Equip,  # Adjust data type if needed
                    "Type_Gardiennage": Type_Gardiennage,
                    "Commune": Commune,
                    "Etat": Etat,
                    "D_Mise_en_Air": D_Mise_en_Air,
                    "Propriétaire": Propriétaire,
                }
                records.append(record)

        for record in records:
            print(record)
            Mobilis.objects.get_or_create(**record)