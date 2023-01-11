# from paths import MODELS_PATH
# from src.models import *
from src.models.all_class import *
import hashlib
# from src.models.artist import Artist, create_table_artist
# from src.models.song import Song, create_table_song

from sqlmodel import create_engine, Session, select
import sqlalchemy
import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    database_user: str
    password: str
    database_name: str
    database_address: str

    class Config:
        env_file = ".env"

db_address = 'ceri-m1-ecommerce-2022:europe-west1:mysql-primary'  # e.g. 'project:region:instance'
settings = Settings()
# connection_name = 'ceri-m1-ecommerce-2022:europe-west1:mysql-primary'
db_user = os.environ.get("DATABASE_USER")   # config('DATABASE_USER')  # e.g. 'my-db-user'
db_pass = os.environ.get("PASSWORD") # config('PASSWORD') # os.environ["PASSWORD"]  # e.g. 'my-db-password'
db_name = os.environ.get("DATABASE_NAME") # config('DATABASE_NAME') # os.environ["DATABASE_NAME"]  # e.g. 'my-database'
DATABASE_URL = sqlalchemy.engine.url.URL.create(
    drivername="mysql+pymysql",
    username=db_user,
    password=db_pass,
    database=db_name,
    # host="localhost", ## Need this to try the connection at the database in local.
    # port=3306,        ## this two will be comment for the deployment.
    query={"unix_socket": "{}/{}".format("/cloudsql", db_address)},
)
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(DATABASE_URL)
# engine = create_engine(sqlite_url, echo=True)
class Database:

    def create_all_tab():
        print('URL: ', DATABASE_URL)
        # print('Yes: ', connection_name)
        create_all_table(engine)


    def remove_all_tab():
        remove_table(engine)

    def get_all_songs():
        with Session(engine) as session:
            statement = select(Song)
            results = session.exec(statement).all()
            for song in results:
                print(song)
            return(results)

    def get_all_albums():
        with Session(engine) as session:
            statement = select(Album)
            results = session.exec(statement).all()
            for album in results:
                print(album)
            return(results)

    def get_all_artists():
        with Session(engine) as session:
            statement = select(Artist)
            results = session.exec(statement).all()
            for artist in results:
                print(artist)
            return(results)

    def insert_song(new_name, new_id_artist, new_id_album):
        new_song = Song(id_album=new_id_album, id_artist=new_id_artist, name=new_name)
        session = Session(engine)
        session.add(new_song)
        session.commit()
        session.refresh(new_song)

    def insert_album(new_name, new_id_artist, new_image, new_release_date, new_type, new_price):
        new_album = Album(name=new_name, id_artist=new_id_artist, image=new_image, release_date=new_release_date, type=new_type, price=new_price)
        session = Session(engine)
        session.add(new_album)
        session.commit()
        session.refresh(new_album)

    def insert_artist(new_firstname, new_secondname, new_nationality):
        new_artist = Artist(firstname=new_firstname, secondname=new_secondname, nationality=new_nationality)
        session = Session(engine)
        session.add(new_artist)
        session.commit()
        session.refresh(new_artist)

    def get_songs_from_album(id_to_search):
        with Session(engine) as session:
            statement = select(Album).where(Album.id == id_to_search)
            result = session.exec(statement).one()
            print(result)
            # for song in results.songs:
            #     print(song)
            return(result)
    
    def insert_user(username: str, password: str, image: str, firstname: str, is_admin: int):
        new_user = User(username=username, password= hashlib.sha256(password.encode('utf-8')).hexdigest(), firstname=firstname, image=image, is_admin=is_admin)
        session = Session(engine)
        session.add(new_user)
        print(new_user)
        session.commit()
        session.refresh(new_user)
        print("User added :", new_user)
        Database.create_cart(new_user, session)
        return new_user
        
        

    def connect_user(username, password):
        resp = {'message': str, 'status': int, 'user': User}
        with Session(engine) as session:
            statement = select(User).where(User.username == username)
            result = session.exec(statement)

            print("test=",result)
            if(len(result.all()) == 0):
                resp['message'] = "Nom d'utilisateur inexistant"
                resp['status'] = 404
            else:
                statement = select(User).where(User.username == username, User.password == hashlib.sha256(password.encode('utf-8')).hexdigest())
                result = session.exec(statement).one_or_none()
                if(result == None):
                    resp['message'] = "Mot de passe incorrect"
                    resp['status'] = 404
                else:
                    user = result
                    resp['message'] = "Bienvenue " + user.firstname
                    resp['status'] = 200
                    resp['user'] = user
        return resp

    def modify_user_profil(user: User):
        resp = {'message': str, 'status': int, 'new_user': User}
        with Session(engine) as session:
            statement = select(User).where(User.id == user.id)
            user_finded = session.exec(statement).one_or_none()
            if(user_finded == None):
                resp['message'] = "Utilisateur non trouvé"
                resp['status'] = 404
            else:
                print("user finded", user_finded)
                user_finded.username = user.username
                user_finded.image = user.image
                session.add(user_finded)
                session.commit()
                session.refresh(user_finded)
                resp['message'] = "Utilisateur modifier"
                resp['status'] = 202
                resp['user'] = user_finded
        return resp
    
    def get_all_users():
        with Session(engine) as session:
            statement = select(User)
            results = session.exec(statement).all()
            for user in results:
                print(user)
            return(results)
    
    def create_cart(user: User, session: Session):
        new_cart = Cart(user_id=user.id)
        session.add(new_cart)
        session.commit()
        session.refresh(new_cart)
        user.id_command_in_process = new_cart.id
        session.commit()
        session.refresh(user)
        print("Cart added: at the user : ", user)

    def validate_cart(user: User):
        resp = {'message': str, 'status': int, 'user': User}
        with Session(engine) as session:
            statement_to_get_current_user = select(User).where(User.id == user)
            current_user = session.exec(statement_to_get_current_user).one_or_none()
            if(current_user == None):
                resp['status'] = 404
                return resp
            statement = select(Cart).where(Cart.id == current_user.id_command_in_process)
            command_in_process = session.exec(statement).one_or_none()
            if(command_in_process == None):
                resp['status'] = 402
            else:
                command_in_process.is_paid = 1
                session.add(current_user)
                Database.create_cart(current_user, session)
                resp['message'] = "Paiement effectué"
                resp['status'] = 202
                resp['user'] = current_user
            return(resp)

    def create_product(cart: Cart, album: Album, session: Session):
        new_product = Product(id_album=album.id, id_cart=cart.id, price=album.price)
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        print("new product", new_product)
        cart.price += new_product.price
        session.commit()
        session.refresh(cart)
        print("Product added at the cart : ", cart.products)
        print("Price : ", cart.price)
    
    def add_product_to_the_user_cart(user: User, album: Album):
        print()
        resp = {'message': str, 'status': int, 'cart': Cart}
        with Session(engine) as session:
            statement_to_get_current_user = select(User).where(User.id == user)
            current_user = session.exec(statement_to_get_current_user).one_or_none()
            if(current_user == None):
                resp['status'] = 404
                return resp
            statement = select(Cart).where(Cart.id == current_user.id_command_in_process)
            command_in_process = session.exec(statement).one_or_none()
            if(command_in_process == None):
                resp['status'] = 402
                return resp
            statement = select(Album).where(Album.id == album)
            album_for_product = session.exec(statement).one_or_none()
            if(album_for_product == None):
                resp['status'] = 402
            else:
                Database.create_product(command_in_process, album_for_product, session)
                session.add(current_user)
                session.refresh(current_user)
                resp['message'] = "Produit ajouté au panier"
                resp['status'] = 202
                resp['cart'] = command_in_process
            return(resp)
    
    def get_cart_from_user(user: int):
        resp = {'message': str, 'status': int, 'cart': Cart, 'products': List[Product]}
        with Session(engine) as session:
            statement_to_get_current_user = select(User).where(User.id == user)
            current_user = session.exec(statement_to_get_current_user).one_or_none()
            if(current_user == None):
                resp['status'] = 404
                return resp
            statement = select(Cart).where(Cart.id == current_user.id_command_in_process)
            command_in_process = session.exec(statement).one_or_none()
            if(command_in_process == None):
                resp['status'] = 402
                return resp
            else:
                products = command_in_process.products
                resp['message'] = "Liste des produits du panier"
                resp['status'] = 202
                resp['cart'] = command_in_process
                resp['products'] = products
            return(resp)
            
    def remove_product_from_cart(product: int):
        resp = {'message': str, 'status': int}
        with Session(engine) as session:
            statement = select(Product).where(Product.id == product)
            product = session.exec(statement).one_or_none()
            if(product == None):
                resp['message'] = "Produit non trouvé"
                resp['status'] = 404
            else:
                resp['message'] = "Produit supprimer du panier"
                resp['status'] = 200
                session.delete(product)
                session.commit()
        return(resp)

# def main():
#     Database.create_all_tab()

# main()