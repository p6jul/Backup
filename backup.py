#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Script de sauvegarde d'un site internet  et de sa BDD vers un FTP

### Importation de la biblioteque des modules qui va permettre d'utiliser des definitions et des instructions ###
print("Importation des modules")
#Import des modules qui gerent les fichiers et les dossiers
import os
import shutil 
#Import des modules qui gerent le temps (date,heure)
import time
import datetime
#Import des modules qui gerent des programmes externes a python
import subprocess
from subprocess import check_call
import sys
print("Importation terminee")
### ###

### Creation des variables ###
print("Lecture des variables")
# Date du jour
date = (time.strftime("%d-%m"))

###############################################################
# Entrer vos parametres a la place des characteres ********** #
###############################################################

# Informations FTP
ipftp = '**********'
userftp = '********'
mdpftp = '**********'
portftp = '********'

# Informations MySQL
usersql = '**********'
mdpsql = '*********'
hostsql = '*********'
basesql = '********'

# Nom du site
site_name = '******'

# Dossier de destination du backup local
destdir = '********'

# Dossier de destination du dump SQL
destsql = '***********'

# Dossier du site internet a sauvegarder
site_dir = '************'

###########################################
# Ne plus rien modifier apres cette ligne #
###########################################

# Nom du fichier de Backup
backup_file = date+site_name+'.tar.gz'

print("Fin de lecture des variables")
### ###

# Creation des repertoires de destination
print("Creation des repertoires")
os.makedirs(destdir, exist_ok=True)
os.makedirs(destsql, exist_ok=True)
print("Creation terminee")

# Verification des paquets requis et mise a jour
print("Verification des paquets requis")
check_call(['apt-get', 'install', '-y', 'lftp'])
check_call(['apt-get', 'install', '-y', 'tar'])
check_call(['apt-get', 'install', '-y', 'gzip'])
print("Verification terminee")

# Dump de la base SQL
print("Dump de la base SQL")
os.system("mysqldump --opt -q -f -h "+hostsql+" -u "+usersql+" -p"+mdpsql+" --all-databases > "+destsql+'/'+basesql+".sql")
print("Dump terminee")
time.sleep(1)

# Creation du backup en .tar.gz
print("Compression du backup")
subprocess.call(['tar', '-czf', backup_file, site_dir, destsql])
print("compression terminee")
time.sleep(1)

# Envoie du backup vers le FTP
print("Upload du backup vers le FTP")
os.system("lftp "+userftp+":"+mdpftp+"@"+ipftp+":"+portftp+" -e 'put "+backup_file+"; exit'")
print("Upload terminee")

# Deplacement du backup vers le dossier backup
print("Deplacement du backup pour une sauvegarde local")
shutil.move(backup_file,destdir)

# Suppression du dump SQL
print("Suppression du dump SQL")
shutil.rmtree(destsql)

# Decommenter la derniere ligne si vous ne voulez pas garder une sauvegarde en local
# Pour decommenter une ligne suprimer le cararactere '#' en debut de ligne

# Suppression du Backup local
#shutil.rmtree(destdir)
