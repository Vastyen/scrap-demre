from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
import sqlite3

con = sqlite3.connect("puntajes.db")
cursor = con.cursor()

def getData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('td', class_='')
    datos = []
    for i in range(0, len(data)):
        if (str(data[i]) != ""):
            oldString = str(data[i])
            newString = oldString.replace('<td>', '')
            oldString = newString
            newString = oldString.replace('</td>', '')
            newString = newString.strip()
            if newString:
                datos.append(newString)
    cont = 0
    listaTemp = []
    for i in range(0, len(datos)):
        listaTemp.append(datos[i])
        cont = cont + 1
        if cont == 5:
            if listaTemp != ['0,00', '0,00', '0,00', '0,00', '0,00']:
                universidad = listaTemp[0]
                carrera = listaTemp[1]
                ciudad = listaTemp[2]
                region = listaTemp[3]
                puntaje = listaTemp[4]

                if puntaje == '0,00':
                    puntaje = 'NO EXIGE'
                push = """INSERT INTO puntajes (universidad, carrera, ciudad, region, puntaje) VALUES (?, ?, ?, ?, ?)"""
                variables = (universidad, carrera, ciudad, region, puntaje)

                cursor.execute(push, variables)
                con.commit()
                print("Scrapeando...")
                listaTemp = []
                cont = 0


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=1"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=2"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=4"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=5"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=6"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=8"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=10"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=12"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=13"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=14"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=15"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=16"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=209"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=artes&subArea=201"
getData(url)


url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=17"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=18"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=19"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=20"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=21"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=22"
getData(url)

url = "https://mizonapreu2017.preupdv.cl/buscadorCarreras/buscadorCarreraNuevoExterno.html?area=bioquim&subArea=23"
getData(url)
