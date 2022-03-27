from distutils.debug import DEBUG
from flask import Flask, jsonify
from flask_mysqldb import MySQL

from config import conexion

app = Flask(__name__)


@app.route('/parcial_1')#ruta de la funcion
def listar_peliculas():
   try:
            with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
             cursor.execute("select Codpelicula,NombrePelicula,FraseActor,CodGenero from Peliculas;")
             datos=cursor.fetchall()
             peliculas=[]
             for fila in datos:
                pelicula={'Codpelicula':fila[0],'NombrePelicula':fila[1],'FraseActor':fila[2],'CodGenero':fila[3]}
                peliculas.append(pelicula)
             return jsonify({'peliculas en estreno':peliculas,'mensaje':"Estos son las peliculas en estreno."})
   except Exception as e:
    return jsonify({'Mensaje':"Error al listar"})

@app.route('/condicionado')
def listar_peliculas_condicion():
   try:
            with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
             cursor.execute("select Codpelicula,NombrePelicula,FraseActor,CodGenero from Peliculas \
                           where Codpelicula=1111;")
             datos=cursor.fetchall()
             peliculas=[]
             for fila in datos:
                pelicula={'Codpelicula':fila[0],'NombrePelicula':fila[1],'FraseActor':fila[2],'CodGenero':fila[3]}
                peliculas.append(pelicula)
             return jsonify({'pelicula por condicion':pelicula,'mensaje':"Esta es la pelicula encontrada."})
   except Exception as e:
    return jsonify({'Mensaje':"Error al listar"})
