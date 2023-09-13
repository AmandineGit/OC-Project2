import csv23 as csv
# import upload
import os

# Varibales globales
compteur = 0


def csv_creationwithentete(entete, datas, name_csv):
    # fonction de création d'un csv à partir des données retournées par upload.info_livre(urlexo2)
    if os.path.exists(name_csv):
        with open(name_csv, 'a') as CSV1livre:
            writer = csv.writer(CSV1livre)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        print('Le fichier CSV : ', name_csv, ' a été mis à jour.')
    else:
        global compteur
        with open(name_csv, 'w') as CSV1livre:
            writer = csv.writer(CSV1livre)
            headers = entete
            writer.writerow(headers)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        compteur = compteur + 1
        print('Le fichier CSV : ', name_csv, ' a été crée.')


# ---------------------- Test unitaires ----------------------------------#
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# global nom_csv
# csv_creationwithentete(upload.datas_entete, upload.info_livre(urlexo2), 'catego_test.csv')
