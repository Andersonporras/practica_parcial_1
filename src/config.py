from distutils.command.config import config
from distutils.debug import DEBUG
from flask_mysqldb import MySQL


import pyodbc
direccion_servidor = 'DESKTOP-N66NP2L\SQL2017'
nombre_bd = 'BDCINE01'
nombre_usuario = 'apr'
password = '8769'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)