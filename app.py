import requests
from bs4 import BeautifulSoup
import datetime
import pytz
from winotify import Notification
import tkinter as tk
from tkinter import ttk
from datetime import datetime



# Obter informações do clima 

def obter_clima(cidade):
    API_KEY = "1e95d8e167c2fd18818bb85e0d6fc4e0"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    try:
        requisicao = requests.get(link)
        requisicao.raise_for_status()
        requisicao_dic = requisicao.json()

        descricao = requisicao_dic['weather'][0]["description"]
        temperatura = requisicao_dic['main']['temp'] -273.15
        umidade = requisicao_dic['main']['humidity']
        vento = requisicao_dic['wind']['speed']


        return descricao, temperatura, umidade, vento
    except requests.exceptions.RequestException as e:
        return None, None, None, None
    

# Atualizar e exibir informações do clima
def atualizar_clima():
    cidade = cidade_entry.get()
    descricao, temperatura, umidade, vento = obter_clima

    if descricao:
        clima_info.set(f"Localização {cidade}\n"
                       f"Descrição: {descricao.capitalize()}\n"
                       f"Temperatura: {temperatura:.2f}°C\n"
                       f"Umidade: {umidade}%\n"
                       f"Vento: {vento} m/s")
        
    else:
        clima_info.set("Não foi possível obter as informações do clima.")

# Atualizar data e hora
def atualizar_data_hora():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data_hora.set(f"Data e Hora: {agora}")
    root.after(1000, atualizar_data_hora)


# Configurações da interface gráfica
root = tk.Tk()
root.title("Aplicativo de Previsão do tempo")