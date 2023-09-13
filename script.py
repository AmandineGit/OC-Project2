
import geturlsslist
import upload
import usecsv

# Variables globales
nom_csv = 'fichier.csv'
url = 'https://books.toscrape.com/'


# pour chaque url de links_catego_livres j'execute upload.info_livre puius csv_creation et les données s'ajoute dans le même fichier csv
def csv_datas_livresbycatego():
    liste = geturlsslist.namelinks_allbooks
    # decommenter si besoin de test sur une liste restreinte
    # liste = listetest
    for line in range(len(liste)):
        listline = liste[line]
        catego = listline[0]
        url_livre = listline[1]
        global nom_csv
        nom_csv = 'catego' + '_' + catego + '.csv'
        print('le lien est : ', url_livre)
        usecsv.csv_creationwithentete(upload.datas_entete, upload.info_livre(url_livre), nom_csv)
    print(usecsv.compteur, 'fichiers CSV ont été crées.')


# ------------------- Lancement du programme -----------------------------#
# geturlsslist.urls_catego_livres(geturlsslist.recup_urlallpages(geturlsslist.recup_catego(url)))
# csv_datas_livresbycatego()


# ---------------------- Test unitaires ----------------------------------#

# ----------execution de urls_catego_livres depuis script.py pour charger la variable namelinks_allbooks ou la fournir en retour
# geturlsslist.urls_catego_livres(geturlsslist.recup_urlallpages(geturlsslist.recup_catego(url)))

# ----------execution de csv_datas_livresbycatego avec un echantillon
# listetest = [['mystery_3', 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'],['travel_2', 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html']]
# csv_creationwithentete(entete, datas, name_csv)
# csv_datas_livresbycatego()
# les print sont à de-commenter dans la boucle dans la boucle
# print('nom csv : ', nom_csv)
# print('le lien est : ',url_livre)

# ----------execution de info_livre avec une url de test
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# print(upload.info_livre(urlexo2))
# print(upload.datas_entete)
# print(upload.datas_content)
