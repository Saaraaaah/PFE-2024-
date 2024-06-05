from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

if start_point and end_point and data_route:
    # Créez la carte de base centrée sur des coordonnées spécifiques avec le niveau de zoom et le contrôle de l'échelle
            midpoint_lat = (float(start_point[0]) + float(end_point[0])) / 2
            midpoint_lon = (float(start_point[1]) + float(end_point[1])) / 2
            midpoint = (midpoint_lat, midpoint_lon)
        
        if print == True:
            map=folium.Map(location= midpoint if midpoint is not None else [latitude,logitude],zoom_control=False,zoom_start=zoom_start,control_scale=False,  width=width, height=height)
        else:
            
            map=folium.Map(location= midpoint if midpoint is not None else [latitude,logitude],zoom_control=True,zoom_start=zoom_start,control_scale=True,  width=width, height=height)
            Draw(export=True).add_to(map)
            MousePosition().add_to(map)
            MiniMap(toggle_display=True).add_to(map)
            map.add_child(MeasureControl())
            
            Fullscreen().add_to(map)
            LocateControl().add_to(map)
            Geocoder().add_to(map)
            js=gpd.read_file("DZA_adm2.geojson")  # Charger les données des limites administratives à partir du fichier GeoJSON
            style={'fillColor':'#FF0000',          # Définir les styles par défaut pour les limites
            'lineColor':'#c9d91e'
            }
            js=folium.GeoJson(    # Créez une couche GeoJSON avec des informations de style et d'info-bulle
                        js,
                        name="Limite administrative de Bouira ", # Définir le nom de la couche (« Limite administrative de Bouira »)
                        style_function=lambda x:get_zone_color(x), # Appliquer la fonction de couleur de remplissage aléatoire
                        tooltip=folium.GeoJsonTooltip(
                        fields=["ID_0", "ISO", "NAME_0","ID_1","NAME_1","ID_2","NAME_2", "TYPE_2","ENGTYPE_2","NL_NAME_2","VARNAME_2"],
                        aliases=["ID_0", "ISO", "NAME_0","ID_1","NAME_1","ID_2","NAME_2", "TYPE_2","ENGTYPE_2","NL_NAME_2","VARNAME_2"],
                        localize=True
                        )).add_to(map) 
            citysearch = Search(
            layer=js,
            geom_type="Point",
            placeholder="Search for a US City",
            collapsed=True,
            search_label="NAME_2",
            ).add_to(map)