from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy


# Este método se encarga de configurar la conexión con la base de datos
def get_db():
    platzi_db = current_app.config['PLATZI_DB_URI']
    client = MongoClient(platzi_db) #crear cliente de mongo
    return client.platzi #platsi se llamara nuestra base de datos


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def test_connection():
    return dumps(db.collection_names())


def collection_stats(collection_nombre):
    return dumps(db.command('collstats', collection_nombre))

# -----------------Carreras-------------------------


def crear_carrera(json):
    return str(db.carreras.insert_one(json).inserted_id)
    #lo ultimo hace que retorne el id


def consultar_carrera_por_id(carrera_id):
    #dumps para BSON a JSON
    return dumps(db.carreras.find_one({'_id':ObjectId(carrera_id)}))


def actualizar_carrera(carrera):
    # Esta funcion solamente actualiza nombre y descripcion de la carrera
    return str(db.carreras.update_one({'_id':ObjectId(carrera['_id'])},
    {'$set':{'nombre':carrera['nombre'], 'descripcion':carrera['descripcion']}}))
    # se puede retornar el cout de modificaciones con
    #.modified_count


def borrar_carrera_por_id(carrera_id):
    return str(db.carreras.delete_one({'_id':ObjectId(carrera_id)}))


# Clase de operadores
def consultar_carreras(skip, limit):
    return dumps(db.carreras.find({}).skip(int(skip)).limit(int(limit)))


def agregar_curso(json):
    return str('Falta por implementar')


def borrar_curso_de_carrera(json):
    return str('Falta por implementar')

# -----------------Cursos-------------------------


def crear_curso(json):
    return str('Falta por implementar')


def consultar_curso_por_id(id_curso):
    return str('Falta por implementar')


def actualizar_curso(curso):
    # Esta funcion solamente actualiza nombre, descripcion y clases del curso
    return str('Falta por implementar')


def borrar_curso_por_id(curso_id):
    return str('Falta por implementar')


def consultar_curso_por_id_proyeccion(id_curso, proyeccion=None):
    return str('Falta por implementar')


def consultar_curso_por_nombre(nombre):
    return str('Falta por implementar')

