from django.http import HttpResponse ,HttpResponseRedirect  #fournit des utilitaires pour gérer les requêtes et les réponses HTTP.
from django.shortcuts import render,redirect
import folium
from .tasks import get_user_location, find_nearest_posta, get_shortest_route, generate_map_with_user_and_posta

import base64
from .tasks import *
from .forms import *
from .models import Profile
from django.http.response import JsonResponse
import os
from PIL import Image as PilImage
from folium import TileLayer     #bibliothèque principale pour créer des cartes Web interactives.
from core.models import Djezzy, Posta,Mobilis,Ooredoo2,Algerie_Telecom,Service_Universel  #importe des modèles
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder #classes des plugins folium pour ajouter des fonctionnalités telles que des calques
import geopandas as gpd #bibliothèque permettant de travailler avec des données géospatiales dans des trames de données de type pandas.
import random #utilisé pour générer des couleurs aléatoires dans le code.
from django.contrib.auth import authenticate,login,logout #Fournit des fonctions d'authentification des utilisateurs (connexion, déconnexion).
from django.contrib.auth.models import User #importe le modèle User pour la gestion des utilisateurs.
from folium.plugins import MousePosition ,MiniMap,MeasureControl #plugins supplémentaires pour afficher la position de la souris
from geopy.distance import distance ,geodesic
from django.template.loader import render_to_string
from folium.plugins import Draw
from folium.plugins import Search
from django.conf import settings
##################################################################################################
def carte(request):
    return render(request, 'cartographie.html')

#def api_view(request):
   
 
    #return render(request, 'sss.html')


def homePage(request):
	return render(request,'index.html')

##################################################################################################


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        


        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render(request, 'signup.html')


##################################################################################################

def LoginPage(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass']
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/responsable')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request,'login.html')



##################################################################################################


def LogoutPage(request):
    logout(request)
    return redirect('login')



##################################################################################################
# Create your views here.
    
def choose_cat(cat):
    if cat=='posta':
        return Posta.objects.all()
    elif cat=='Mobilis':
        return Mobilis.objects.all()
    elif cat=='Algerie_Telecom':
        return Algerie_Telecom.objects.all()
    

##################################################################################################


#Fonction pour générer une couleur de remplissage aléatoire pour les zones



blue_tile = TileLayer(
         tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
         attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
         name='Blue Map',
         overlay=True,
         opacity=0.7
    )






def generate_image_and_save(request):
   
    from .tasks import generate_image, respo
    from .models import Profile
    from django.http.response import JsonResponse

    print(0000000000000000)
    map_html = respo()  
    print(111111111)
    path_image = generate_image(request=request, html_content=map_html)
    print(path_image)
    print(2222222222222)
    profile, state = Profile.objects.get_or_create(user=request.user)
    
    if profile:
        image_url =  profile.image.url
        print (image_url)
        return JsonResponse({'image_data':  profile.image.url})
    
    return JsonResponse({'error': 'Image not found'}, status=404)


def generate_map_view(request):
    if request.method == 'POST':
        user_location = get_user_location(request)
        category =  request.POST.get('category')
        nearest_posta = find_nearest_posta(user_location,category)
        posta_location = (nearest_posta[0].latitude, nearest_posta[0].longitude)
        route_geometry = get_shortest_route(user_location, posta_location)
        my_map = generate_map(user_location, posta_location, route_geometry,category)
        return render(request, 'index.html', {'my_map': my_map})
    else:
        my_map = generate_map(user_location=None, posta_location=None, route_geometry=None,category=None)
        return render(request, 'index.html', {'my_map': my_map})
        


def index(request):
     
    form_generate_Image=Generate_image()
    context={'form_generate_Image':form_generate_Image}
    return render(request, 'ind.html', context)

from django.http import HttpResponse
from .tasks import respo

def responsable(request):
    # Utilisez la fonction respo pour générer votre carte
    map_html = respo()

    # Retournez la carte sous forme de réponse HTTP
    return HttpResponse(map_html)


from django.contrib.auth.models import User, Permission, ContentType,Group
from django.contrib.contenttypes.management import create_contenttypes
from django.contrib.auth.decorators import permission_required,login_required
from .models import Permission_user
#@login_required
#@permission_required('can_add_log_entry')
def user_perm(request):
    per = 'can add map'
    user = request.user
    result = Permission_user.objects.filter(user=user, permission=per).exists()
    if result:
        return HttpResponse('sucsess')
    else:
        return redirect('responsable')
        
    
