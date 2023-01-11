import mariadb
from os import environ
import sys

USER=environ.get("USER")
PASSWORD=environ.get("PASSWORD")
DBNAME=environ.get("DBNAME")
HOST=environ.get("HOST")
MYSQL_PORT=3306



try:
   connection = mariadb.connect(user=USER, password=PASSWORD, database=DBNAME, unix_socket= "/cloudsql/ceri-m1-ecommerce-2022:europe-west1:mysql-primary", port=int(MYSQL_PORT))
   print("Connexion à la bdd réussie")
except mariadb.Error as e:
    print(f"Impossible de se connecter à la bdd : {e}")
    sys.exit(1)
