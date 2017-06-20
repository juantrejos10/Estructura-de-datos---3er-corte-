#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Autores: Elkin Camilo Osorio MArtinez y Juan Pablo Trejos Rodriguez
#Programa: pokeapi.py
#Descripcion: Este programa consulta y muestra una lista de pokemones almacenados en un repositorio en la pagina web : www.pokeapi.co
#Fecha: 16/06/2017 4:30 pm

import requests

def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
	args = {'offset' : offset} if offset else {}

	response = requests.get(url, params=args)

	if response.status_code == 200:

		payload = response.json()
		results = payload.get('results', [])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)

		next = raw_input("¿Continuar listando? [Y/N]").lower()
		if next == 'y':
			get_pokemons(offset=offset+20)

if __name__ == '__main__':
	url = 'http://pokeapi.co/api/v2/pokemon-form/'
	get_pokemons()

