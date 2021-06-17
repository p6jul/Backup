# Backup
Backup est un scripte en Python.

Il a été test sous les distributions Linux Debian 9 et 10.


# Description
Il permet de faire une sauvegarde de votre site internet et de sa base de données compressée en tar.gz.

La sauvegarde portera le nom de la date du jour et le nom de votre site.

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

Remplacer les caractères **** par vos paramètres

#Informations FTP
1) ipftp = '******'     Rentrer l'addresse Ip ou le nom d'hote du serveur FTP
2) userftp = '******'     Rentrer le nom d'utilisateur 
3) mdpftp = '******'    Rentrer le mot de passe
4) portftp = '******'     Rentrer le port. Par defaut c'est '21'

#Informations MySQL
1) usersql = '******'   Rentrer le nom d'utilisateur de votre base de données
2) mdpsql = '******'    Rentrer le mot de passe de votre base de données
3) hostsql = '******'   Rentrer le nom de votre serveur. Par defaut vous pouvez rentrer 'localhost'
4) basesql = '******'   Rentrer le nom de votre base de données

#Nom du site 
1) site_name = '******'    Rentrer le nom de votre site

#Dossier de destination du backup local 
1) destdir = '******' Rentrer le chemin du dossier où sera stocker la sauvegarde en local. Exemple: '/backupsite'     

#Dossier de destination du dump SQL
1) destsql = '******' Rentrer le chemin du dossier qui servira a la sauvegarde de la BDD. Exemple:'/backupsite/sql'

!!! Attention !!! Le dossier sera supprimé à la fin. Considéré ce dossier comme un dossier temp

#Dossier du site internet a sauvegarder 
1) site_dir = '******' Rentrer le chemin du dossier de votre site internet. Exemple: '/var/www/html'

# Option
Par défaut le script garde aussi une sauvegarde en local. 

Si vous ne voulez pas la garder et donc la supprimer décommenter la derniere ligne du script "#shutil.rmtree(destdir)".

Pour décommenter une ligne supprimer le caractère "#" en début de ligne


# Exécution
Pour exécuter le script taper la commande :/# sudo python3 backup.py

# Erreur d'exécution
Selon, comment vous avez importé le script (exemple de Windows vers une machine virtuel Linux)

Ou éditer le script avec certain éditeur (exemple visual studio code)

Vous pouvez avoir une erreur d'exécution à cause des caractères non reconnus.

Il faut installer le paquet dos2unix avec la commande:/#sudo apt-get install dos2unix

Et ensuite executer la commande :/#sudo dos2unix backup.py

# Automatisation du script
Vous pouvez automatiser l'exécution du script avec Crontab.

Par exemple pour que le script s'exécute tous les jours à 23h30.

Dans la console, vous tapez la commande ;/# sudo crontab -e

Votre éditeur de texte apparaît et vous rentrez : 30 23 * * * /root/python3 backup.py

