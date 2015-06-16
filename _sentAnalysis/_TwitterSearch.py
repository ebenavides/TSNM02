##Se importan las librerias

from TwitterSearch import *
from pymongo import MongoClient
from Tweet import Tweet
from collections import deque
from bson.binary import Binary
import pickle
import time


##En esta definicion de funcion se llama la funcion definida en donde se consulta los tweets
def my_callback_closure(current_ts_instance): 
    queries, tweets_seen = current_ts_instance.get_statistics()
    if queries > 0 and (queries % 5) == 0: 
        time.sleep(60)
        
try:
    # PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
    mongoClient = MongoClient('localhost',27017)

    # PASO 2: Conexión a la base de datos
    db = mongoClient.Twitter

    # PASO 3: Obtenemos una coleccion para trabajar con ella
    collection = db.Tweets

    # PASO 4: Se invoca la funcion de busqueda de tweets
    tso = TwitterSearchOrder()
    # PASO 5: Se define la palabra clave para las búsquedas de tweets
    tso.set_keywords(['Keylor Navas'])
    # PASO 6: Se define el idioma para las búsquedas de tweets
    tso.set_language('es') 
    tso.set_include_entities(False) 

    # PASO 7: Se define las llaves de acceso a la aplicacion de Twitter
    ts = TwitterSearch(
        consumer_key = '1uQQd0wTVH76kCPCqNVnm15Lk',
        consumer_secret = 'XNTLr9Y2S1ThRYlGQyKxoOkIVUuheAMrHFmpyFwIQZiyBKU8hT',
        access_token = '898572810-btveERSAL1n5BflyJL54ZzylIKFeV4xA14vXPcaq',
        access_token_secret = '5bO2B8PsxiPiQeGaUL0ESGoZSCTMa4n2tvNkaZ39J1tYZ'
     )

    # PASO 8: Escribimos todos los documentos de la base de datos
    num_tweets = 0
    
    lista = {}
    for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
        if  num_tweets < 5000:

            elemento = ( str('@%s tweeted: %s' % ( tweet['user']['screen_name'].encode("utf-8", errors='ignore'), tweet['text'].encode("utf-8", errors='ignore'))))
            print(elemento)
            print("")
            lista[str(num_tweets)]=(elemento)
            collection.insert(lista)
            print(lista)
            print("")
            cursor = collection.find()
            for fut in cursor:
                print (fut)
            
            num_tweets = num_tweets + 1

        
    # PASO 9: Cerrar la conexion con MongoDB
    
    mongoClient.close()
            
    


except TwitterSearchException as e: 
    print(e)


