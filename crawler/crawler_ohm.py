from json import loads
from time import sleep
from urllib3 import PoolManager
import mysql.connector
from datetime import datetime


class banco():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="aluno",
            password="sptech"
        )

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS prova_marise")

        self.mycursor.execute("USE prova_marise")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS registros (id int primary key auto_increment, registro decimal(4,1), data_registro DATETIME, tipo_medida varchar(1))")

    def insert(self, registro, tipo):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        sql = "INSERT INTO registros VALUES (null, %s, %s, %s)"
        val = (registro, now, tipo)
        self.mycursor.execute(sql, val)

        self.mydb.commit()
        
    def drop_table(self):
        self.mycursor.execute("drop table registros")
        
banco1 = banco()

def conversor(valor):
    return float(valor[0:4].replace(",", '.'))

with PoolManager() as pool:
    while True:
        response = pool.request('GET', 'http://localhost:9000/data.json')
        data = loads(response.data.decode('utf-8'))
        temp_min = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Min'])


        temp_value = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value'])
        banco1.insert(temp_value, "C")
        
        
        temp_max = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Max'])
        
        print(f'Dados inseridos no banco! o valor atual de temperatura: {temp_value}')
        sleep(3)