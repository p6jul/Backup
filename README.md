# Backup
Backup est un script en Python.

Il a été test sous les distributions Linux Debian 9 et 10.


# Description
Il permet de faire une sauvegarde de votre site internet et de sa base de données compressée en tar.gz.

Il envoie la sauvegarde vers un serveur FTP.

Il garde par défaut une sauvegarde en local.


# Prérequis
Debian 9 ou 10

Python 3. Pour l'installer :/#sudo apt-get install python3

# Installation
1) Télécharger le script ou un copier coller dans votre éditeur de texte.
2) Placer le à la racine de votre disque.
3) Mettre les droits d'exécution avec la commande :/#chmod +x backup.py
4) Éditer le script pour enregistrer vos paramètres dans la partie concernée.

# Edition des variables du script
Les Variables a modifier sont signalées entre deux encadrés dans le script.

Remplacer les characteres **** par vos paramètres

#Informations FTP
1) ipftp = '**********'     Rentrer l'addresse Ip ou le nom d'hote du serveur FTP
2) userftp = '********'     Rentrer le nom d'utilisateur 
3) mdpftp = '**********'    Rentrer le mot de passe
4) portftp = '********'     Rentrer le port. Par defaut c'est 21

#Informations MySQL
1) usersql = '**********'   Rentrer le nom d'utilisateur de votre base de données
2) mdpsql = '*********'     Rentrer le mot de passe
3) hostsql = '*********'    R
4) basesql = '********'

#Nom du site 
site_name = '******'

#Dossier de destination du backup local (exemple:'/backupsite')
destdir = '********'

#Dossier de destination du dump SQL (exemple:'/backupsite/sql')
destsql = '***********'

#Dossier du site internet a sauvegarder (par defaut le site est dans: /var/www/html)
site_dir = '************'


# Exécution




/#sudo apt-get install dos2unix

