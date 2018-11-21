
#importamos librerias necesarias
import pymongo
from pymongo import MongoClient
import pandas as pd
import os
import pprint


# Seleccionar directorio

path = "C:/Users/Andrés/Desktop/Proyecto big data/Data"

os.chdir(path)

# Conectando con MongoClient

client = MongoClient('mongodb://miadmongo:u8usclIJ0UGQzu1D8rZnkvwiabUfK7YKFgdbKJ6GT7bxuzRA08rTf1OIBcA2WLs86e80zC12zZXOuCphCCTRnQ==@miadmongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')

# Obteniendo la base de datos

db = client.Bigdata
db = client.test_database


# Obteniendo la colección

collection = db.test_collection
collection = db.Data



