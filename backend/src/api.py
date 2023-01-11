from typing import Union

from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from src.db.database import *
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "Database",
        "description": "Operations with database"
    },
    {
        "name": "Album",
        "description": "Operations with albums.",
    },
    {
        "name": "Song",
        "description": "Operations with songs.",
    },
    {
        "name": "Artist",
        "description": "Operations with artists.",
    },
    {
        "name": "User",
        "description": "Operations with users",
    },
    {
        "name": "Cart",
        "description": "Operations with carts",
    }
]


app = FastAPI(title="Jean Cloud Vinil backend", version=2.0, openapi_tags=tags_metadata)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

#### Root for the database ####
@app.get("/", tags=["Database"], status_code=status.HTTP_200_OK)
def read_root():
    return {'message': 'Jean Cloud Vinyl back is running'}

@app.get('/create/database', tags=["Database"], status_code=status.HTTP_200_OK)
def create_database():
    '''Root to create database'''
    Database.create_all_tab()

@app.get('/drop/database', tags=["Database"], status_code=status.HTTP_200_OK)
def drop_database():
    '''Root to create database'''
    Database.remove_all_tab()

#### Root for songs ####
@app.post("/create/song", tags=["Song"], status_code=status.HTTP_201_CREATED)
def create_song(song: Song):
    '''Root to create a song'''
    Database.insert_song(song.name, song.id_artist, song.id_album)
    return({'message': song})

@app.get("/get/songs", tags=["Song"], status_code=status.HTTP_200_OK)
def read_songs():
    '''Root to get all songs'''
    songs = Database.get_all_songs()
    if(len(songs) == 0):
        return JSONResponse(status_code=404, content={"message": "Aucune musique dans la base de données"})
    return({'message': songs})

#### Root for albums ####
@app.post("/create/album", tags=["Album"], status_code=status.HTTP_201_CREATED)
def create_album(album: Album):
    '''Root to create an album'''
    Database.insert_album(album.name, album.id_artist, album.image, album.release_date, album.type, album.price)
    return({'message': album})

@app.get("/get/albums", tags=["Album"], status_code=status.HTTP_200_OK)
def read_albums():
    '''Root to get albums'''
    albums = Database.get_all_albums()
    if(len(albums) == 0):
        return JSONResponse(status_code=404, content={"message": "Aucun album dans la base de données"})
    return({'message': albums})

@app.get("/get/albumsongs/{album_id}", tags=["Song"])
def read_songs_in_album(album_id: int):
    '''Root to get all songs from an album, use the id of the album (work in progress: need to make with the name)'''
    album = Database.get_songs_from_album(album_id)
    if(len(album.songs) == 0):
        return JSONResponse(status_code=404, content={"message": "Aucune musique dans l'album "+album.name})
    return({'message': album.songs})

#### Root for artist ####
@app.post("/create/artist", tags=["Artist"], status_code=status.HTTP_201_CREATED)
def create_artist(artist: Artist):
    '''Root to create an artist'''
    Database.insert_artist(artist.firstname, artist.secondname, artist.nationality)
    return({'message': artist})

@app.get("/get/artists", tags=["Artist"], status_code=status.HTTP_200_OK)
def read_artists():
    '''Root to get all artists'''
    artists = Database.get_all_artists()
    if(len(artists) == 0):
        return JSONResponse(status_code=404, content={"message": "Aucun artiste dans la base de données"})
    return({'message': artists})

#### Root for user ####
@app.post("/create/user", tags=["User"], status_code=status.HTTP_201_CREATED)
def create_user(username: str, password: str, image: str, firstname: str, is_admin: int):
    '''Root to create an user'''
    user = Database.insert_user(username, password, image, firstname, is_admin)
    return({'message': user})

@app.get("/update/user", tags=["User"], status_code=status.HTTP_202_ACCEPTED)
def modify_user(user: User):
    '''Root to modify an user'''
    msg = Database.modify_user_profil(user)
    return({'message': msg['message'], 'user': msg['user']})

@app.get("/get/user/{username}/{password}", tags=["User"], status_code=status.HTTP_202_ACCEPTED)
def connect_user(username: str, password: str):
    '''Root to connect an user'''
    resp = Database.connect_user(username, password)
    if(resp['status'] == 404):
        return JSONResponse(status_code=404, content={"message": resp['message']})
    return({'message': resp['message'], 'user': resp['user']})

@app.get("/get/users", tags=["User"], status_code=status.HTTP_200_OK)
def get_all_users():
    '''Root to get all users'''
    users = Database.get_all_users()
    if(len(users) == 0):
        return JSONResponse(status_code=404, content={"message": "Aucun utilisateur dans la base de données"})
    return({'message': users})

#### Root for cart ####
@app.post("/validate/cart", tags=["Cart"], status_code=status.HTTP_202_ACCEPTED)
def validate_cart(user: int):
    '''Root to pay the cart in process'''
    resp = Database.validate_cart(user)
    if(resp['status'] == 402 or resp['status'] == 404):
        return JSONResponse(status_code=resp['status'], content={"message": "Le paiement a échoué ou utilisateur non trouvé"})
    return({'message': resp['message'], 'user': resp['user']})
        
@app.post("/add/product", tags=["Cart"], status_code=status.HTTP_200_OK)
def add_product_to_cart(user: int, album: int):
    '''Root to add a product at the command in process (cart)'''
    resp = Database.add_product_to_the_user_cart(user, album)
    if(resp['status'] == 402 or resp['status'] == 404):
        return JSONResponse(status_code=resp['status'], content={"message": "L'ajout du produit a échoué"})
    return({'message': resp['message'], 'cart': resp['cart']})

@app.post("/remove/product", tags=["Cart"], status_code=status.HTTP_200_OK)
def remove_product_from_cart(product_id: int):
    '''Root to remove a product from cart'''
    resp = Database.remove_product_from_cart(product_id)
    if(resp['status'] == 404):
        return JSONResponse(status_code=resp['status'], content={resp['message']})
    return({'message': resp['message']})

@app.get("/get/cart", tags=["Cart"], status_code=status.HTTP_200_OK)
def get_cart(user_id: int):
    '''Root to get the cart of the connected user'''
    resp = Database.get_cart_from_user(user_id)
    if(resp['status'] == 402 or resp['status'] == 404):
        return JSONResponse(status_code=resp['status'], content={"message": "L'utilisateur ou le panier n'existe pas"})
    return({'message': resp['message'], 'products': resp['products'], 'cart': resp['cart']})