# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# #import numpy as np
# import psycopg2

# connection = psycopg2.connect("dbname=Ecommerce user=ceri-commerce password=Elodie host=34.77.160.150 port=5432")
# # connection = psycopg2.connect("dbname=Vinyles user=ceri-commerce password=Elodie host=34.77.160.150 port=5432")

# cursorDatabase = connection.cursor()
# # nbAlbums=0
# # for row in cursorDatabase:
# #     nbAlbums+=row[0]
# # print(nbAlbums)

# query=f'SELECT COUNT(*) FROM public."Album"'
# cursorDatabase.execute(query)
# nbAlbums=0
# for row in cursorDatabase:
#     nbAlbums+=row[0]
# print(nbAlbums+2)

# def getEverything():
#     AllItems=[]

#     # query=f'SELECT "nomAlbum", "nomArtiste" FROM public."Album" NATURAL JOIN public."Artiste" WHERE "nomArtiste" = \'{"Smash Into Pieces"}\''
#     query = f'SELECT "nomAlbum", "nomArtiste", "imageAlbum", "prixAlbum", "quantiteStockAlbum" FROM public."Album" NATURAL JOIN public."Artiste" ORDER BY "nomArtiste", "nomAlbum" ASC'
#     cursorDatabase.execute(query)
#     for row in cursorDatabase:
#         AllItems.append(row[0])
#         AllItems.append(row[1])
#         AllItems.append(row[2])
#         AllItems.append(row[3])
#         AllItems.append(row[4])
#     print(AllItems)
#     print(len(AllItems))

#     #Everything=np.zeros((int(len(AllItems)/5),5), dtype=object)
#     for i in range(0,int(len(AllItems)/5)):
#         for j in range(0,int(len(AllItems)/(nbAlbums+2))+2):
#             Everything[i,j]=AllItems[(i*5)+j]

#     # Everything=np.zeros((int(len(AllItems)/6),6), dtype=object)
#     # for i in range(0,int(len(AllItems)/6)):
#     #     for j in range(0,int(len(AllItems)/6)+2):
#     #         Everything[i,j]=AllItems[(i*6)+j]

#     print(Everything)
#     return Everything.tolist()

# def getAlbumByArtist(nomArtiste):
#     Albums=[]
#     query=f'SELECT "nomAlbum", "imageAlbum", "prixAlbum", "quantiteStockAlbum" FROM public."Artiste" NATURAL JOIN public."Album" WHERE "nomArtiste" =\'{nomArtiste}\'   GROUP BY "nomAlbum","imageAlbum","prixAlbum","quantiteStockAlbum" ORDER BY "nomAlbum" ASC'
#     cursorDatabase.execute(query)

#     for row in cursorDatabase:
#         Albums.append(row[0])
#         Albums.append(row[1])
#         Albums.append(row[2])
#         Albums.append(row[3])
#     #ListeAlbums=np.zeros((int(len(Albums)/4),4), dtype=object)
#     for i in range(0,int(len(Albums)/4)):
#         for j in range(0,int(len(Albums)/4)+2):
#             ListeAlbums[i,j]=Albums[(i*4)+j]

#     return ListeAlbums.tolist()

# def getMusicsByArtist(nomArtiste, nomAlbum):
#     Musiques=[]
#     query=f'SELECT "nomChanson" FROM public."Chanson" NATURAL JOIN public."Album" NATURAL JOIN public."Artiste" WHERE "nomArtiste" =\'{nomArtiste}\' AND "nomAlbum" =\'{nomAlbum}\''
#     cursorDatabase.execute(query)
#     for row in cursorDatabase:
#         Musiques.append(row[0])
#     print(Musiques)
#     return Musiques

# app = FastAPI()
# origins = [
#     "http://localhost:4200",
#     "localhost:4200"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# @app.get("/")
# def read_root():
#     return {"hello":"word"}
#     #return {"Item": getEverything()}

# @app.get("/{nom_artiste}")
# def read_item(nom_artiste: str):
#     print("---------------------------------------------------------------")
#     print(type(nom_artiste))
#     return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}

# @app.get("/{nom_artiste}/{nom_album}")
# def read_item(nom_artiste: str, nom_album: str):
#     print("---------------------------------------------------------------")
#     print(nom_artiste)
#     return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album)}

########################################################################"
# MAIN HELLO WORD QUI MARCHE
# from typing import Union

# from fastapi import FastAPI

# #app = FastAPI()

# app = FastAPI()
# origins = [
#      "http://localhost:4200",
#      "localhost:4200"
#  ]


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

#Main à jour
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mariadb
import identifiantsbdd
import connexion
import commande

connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
cursorDatabase = connection.cursor()


query=f'SELECT * FROM `album`'
cursorDatabase.execute(query)
nbAlbums=0
for row in cursorDatabase:
    nbAlbums+=row[0]
# print(nbAlbums)

def getEverything():
    cursorDatabase = connection.cursor()
    AllItems=[]
    query=f'SELECT nomAlbum, nomArtiste, imageAlbum, prixAlbum, quantiteStockAlbum FROM album NATURAL JOIN artiste ORDER BY nomArtiste, nomAlbum ASC'
    
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    for row in result:
        AllItems.append(row[0])
        AllItems.append(row[1])
        AllItems.append(row[2])
        AllItems.append(row[3])
        AllItems.append(row[4])
    cursorDatabase.close()

    Everything= [0]*int(len(AllItems)/5)
    for i in range(0,int(len(AllItems)/5)):
        Everything[i]=[0]*5
        for j in range(0,int(len(AllItems)/(nbAlbums+2))+4):
            Everything[i][j]=AllItems[(i*5)+j]
    return Everything

def getArtists():
    cursorDatabase = connection.cursor()
    AllArtists=[]
    query=f'SELECT nomArtiste FROM artiste ORDER BY nomArtiste ASC'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    for row in result:
        AllArtists.append(row[0])
        
    cursorDatabase.close()
    # print(AllArtists[0])
    return AllArtists



def getAlbumByArtist(nomArtiste):
    cursorDatabase = connection.cursor()
    Albums=[]
    query=f'SELECT nomAlbum, imageAlbum, prixAlbum, quantiteStockAlbum FROM artiste NATURAL JOIN album WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\')   GROUP BY nomAlbum, imageAlbum, prixAlbum, quantiteStockAlbum ORDER BY nomAlbum ASC'
    cursorDatabase.execute(query)

    for row in cursorDatabase:
        Albums.append(row[0])
        Albums.append(row[1])
        Albums.append(row[2])
        Albums.append(row[3])
    cursorDatabase.close()

    ListeAlbums= [0]*int(len(Albums)/4)
    for i in range(0,int(len(Albums)/4)):
        ListeAlbums[i]=[0]*4
        for j in range(0,int(len(Albums)/4)+2):
            ListeAlbums[i][j]=Albums[(i*4)+j]
    return ListeAlbums

def getMusicsByArtist(nomArtiste, nomAlbum):
    cursorDatabase = connection.cursor()
    Musiques=[]
    query=f'SELECT nomChanson FROM chanson NATURAL JOIN album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\') ORDER BY nomChanson'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        Musiques.append(row[0])
    # print(Musiques)
    cursorDatabase.close()
    return Musiques

def getAlbumImage(nomArtiste, nomAlbum):
    imageAlbum=""
    cursorDatabase = connection.cursor()
    query=f'SELECT imageAlbum FROM album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\')'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        imageAlbum=row[0]
    cursorDatabase.close()
    return imageAlbum

def getAlbumPrice(nomArtiste, nomAlbum):
    prixAlbum=""
    cursorDatabase = connection.cursor()
    query=f'SELECT prixAlbum FROM album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\')'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        prixAlbum=row[0]
    cursorDatabase.close()
    return prixAlbum


app = FastAPI()

origins = [
    "http://localhost:4200",
    "localhost:4200"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Item": getEverything()}

# route en post pour se connecter
@app.post("/connexion")
def login(email: str, password: str):
    print("---------------------------------------------------------------")
    return {connexion.connexion(email, password)}

@app.post("/inscription")
def inscription(nom:str, prenom:str, email:str, password:str, telephone:int, adresse:str, codePostal:int, ville:str, pays:str):
    print("---------------------------------------------------------------")
    return {connexion.inscription(nom, prenom, email, password, telephone, adresse, codePostal, ville, pays)}
    
@app.get("/artistes")
def read_item():
    return {"Artistes": getArtists()}
    
@app.get("/commande")
def read_item(email : str):
    print("---------------------------------------------------------------")
    return {"Email": email, 'Commande': commande.verificationCommande(email)}

@app.get("/{nom_artiste}")
def read_item(nom_artiste: str):
    print("---------------------------------------------------------------")
    return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}


@app.get("/{nom_artiste}/{nom_album}")
def read_item(nom_artiste: str, nom_album: str):
    print("---------------------------------------------------------------")
    return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album), 'Image': getAlbumImage(nom_artiste,nom_album), 'Prix': getAlbumPrice(nom_artiste,nom_album)} 
