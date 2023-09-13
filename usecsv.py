import csv23 as csv
# import upload
import os

# Variables globales
compteur = 0
# info = ['https://books.toscrape.com/catalogue/lust-wonder_191/index.html,0dcadb06206abd3c,Lust & Wonder','£11.87','£11.87','In stock (3 available)','"First came Running with Scissors. Then came Dry. Now, theres Lust &amp; Wonder.In chronicling the development and demise of the different relationships hes had while living in New York, Augusten Burroughs examines what it means to be in love, what it means to be in lust, and what it means to be figuring it all out. With Augustens unique and singular observations and his First came Running with Scissors. Then came Dry. Now, theres Lust &amp; Wonder.In chronicling the development and demise of the different relationships hes had while living in New York, Augusten Burroughs examines what it means to be in love, what it means to be in lust, and what it means to be figuring it all out. With Augustens unique and singular observations and his own unabashed way of detailing both the horrific and the humorous, Lust and Wonder is an intimate and honest memoir that his legions of fans have been waiting for. ...more"','Autobiography','Two','https://books.toscrape.com/media/cache/25/1c/251ce4355601534338a646f2b63be93a.jpg']

def csv_creationwithentete(entete, datas, name_csv):
    # fonction de création d'un csv à partir des données retournées par upload.info_livre(urlexo2)
    # et d'upload du fichier image dans un répertoire
    if not os.path.isdir(datas[-3]):
        category = datas[-3]
        os.mkdir(category)
        print('Le répertoire ' + category + ' a été crée.')

    category = datas[-3]
    chemin_csv = category + '/' + name_csv
    if os.path.exists(chemin_csv):
        with open(chemin_csv, 'a') as CSV1livre:
            writer = csv.writer(CSV1livre)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        print('Le fichier CSV : ', name_csv, ' a été mis à jour.')
    else:
        with open(chemin_csv, 'w') as CSV1livre:
            writer = csv.writer(CSV1livre)
            headers = entete
            writer.writerow(headers)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        global compteur
        compteur = compteur + 1
        print('Le fichier CSV : ', name_csv, ' a été crée.')


# ---------------------- Test unitaires ----------------------------------#
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# global nom_csv
# compteur = 0
# nom_csv = 'links_Mystery.csv'
# csv_creationwithentete(upload.datas_entete, upload.info_livre(urlexo2), nom_csv)
