
from pymongo import MongoClient
from Tweet import Tweet

# Creo una lista de objetos futbolista a insertar en la BD
tweets = [
    Tweet('Iker','Casillas','rojo'),
    Tweet('Carles','Puyol','azul'),
    Tweet('Sergio','Ramos','negro'),
    Tweet('Andrés','Iniesta','morado'),
    Tweet('Fernando','Torres','veige'),
    Tweet('Leo','Baptistao','amarillo')
]


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.Twitter


# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db.Tweets


# PASO 4: CRUD (Create-Read-Update-Delete)

# PASO 4.1: "CREATE" -> Metemos los objetos futbolista (o documentos en Mongo) en la coleccion Futbolista
for tweet in tweets:
    collection.insert(tweet.toDBCollection())



# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()
for tweet in cursor:
    print ("%s - %s - %s" \
          %(tweet['user'], tweet['screen_name'], tweet['text']))

### PASO 4.2.2: "READ" -> Hacemos una Query con condiciones y lo pasamos a un objeto Futbolista
##print ("\n\n*** Buqueda de los futbolistas que sean delanteros ***")
##cursor = collection.find({"demarcacion":{"$in":["Delantero"]}})
##for fut in cursor:
##    print ("%s - %s - %i - %s - %r" \
##          %(fut['nombre'], fut['apellidos'], fut['edad'], fut['demarcacion'], fut['internacional']))
##
##
##
### PASO 4.3: "UPDATE" -> Actualizamos la edad de los jugadores.
##collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)
##
##
##
### PASO 4.4: "DELETE" -> Borramos todos los futbolistas que sean internacionales (internacional = true)
##collection.remove({"internacional":True})
##

# PASO FINAL: Cerrar la conexion
mongoClient.close()
