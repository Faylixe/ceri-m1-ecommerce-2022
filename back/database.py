import mariadb
from os import environ
import sys

# USER=environ.get("USER")
# PASSWORD=environ.get("PASSWORD")
# DBNAME=environ.get("DBNAME")
# HOST=environ.get("HOST")
# MYSQL_PORT=3306

# connection = mariadb.connect(user=USER, password=PASSWORD, database=DBNAME, unix_socket= "/cloudsql/ceri-m1-ecommerce-2022:europe-west1:mysql-primary", port=int(MYSQL_PORT))

# On essaie avec une autre bdd pour voir si le problème vient de là
username='289758'
password='BddEcommerce2022'
database='ceri-ecommerce_bdd'
host='mysql-ceri-ecommerce.alwaysdata.net'
port=3306

try:
    connection = mariadb.connect(user=username, password=password, database=database, host=host, port=port)
    print("Connexion à la bdd réussie")
except mariadb.Error as e:
    print(f"Impossible de se connecter à la bdd : {e}")
    sys.exit(1)
