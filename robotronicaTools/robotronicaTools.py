#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Para lincar esta aplicacion a la terminal.
# sudo ln -s /home/carlosbarreiro/robotronicaTools/robotronicaTools.py /usr/bin/robotronica

# Librerias
import sys
import os # Libreria para poder crear una carpeta
import errno # Por si da error al crear la carpeta
import argparse # Para tomar los argumentos de python
from string import Template # Plantilla a partir de un fichero de texto
import shutil

def createBehaviour():
	# Tomamos las rutas
	pathToolsPy = os.path.realpath(__file__)
	pathTools	= os.path.dirname(pathToolsPy)
	pathCmd 	= os.getcwd()
	# Copiamos la carpeta de proyecto
	shutil.copytree(pathTools+'/resources/proyectoSuper', pathCmd)
	print('Se ha patatitas')
	print(pathTools)
	

# Main de python
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--create", help="Crear un nuevo proyecto", action="store_true")
	parser.add_argument("-b", "--build", help="Compilar un proyecto", action="store_true")
	parser.add_argument("-n", "--name", help="Nombre del proyecto")
	parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
	args = parser.parse_args()

	if args.create:
		print('Se ha creado un nuevo proyecto')
		createBehaviour()
	elif args.build:
		pass
