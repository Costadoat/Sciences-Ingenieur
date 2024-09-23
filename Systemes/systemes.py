# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone
import django
import sys
import os
sys.path.append(os.path.abspath("/home/renaud/Documents/Renaud/GitHub/django_education/"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_education.settings'
django.setup()
from django_education.models import systeme, fichier_systeme

fichiers = fichier_systeme.objects.all()

for fichier in fichiers:
    repertoire=str(fichier.systeme)
    if not os.path.isdir(repertoire):
        os.mkdir(repertoire)
    nom_fichier=repertoire+'/'+str(fichier.nom_fichier)+'.'+str(fichier.type_de_fichier.extension)
    if not os.path.isfile(nom_fichier):
        print('Attention le fichier "'+nom_fichier+'" est manquant.')
