import requests
from bs4 import BeautifulSoup
import datetime
import pytz
from winotify import Notification
import tkinter as tk
from tkinter import ttk

# link do open_weather: https://openweathermap.org/



# CHAMADA DE API E APRESENTAÇÃO DAS INFORMAÇÕES
API_KEY = "1e95d8e167c2fd18818bb85e0d6fc4e0"
cidade = input("Digite o nome da cidade: ")
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

try:
    requisicao = requests.get(link)
    requisicao.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(f"Previsão para {cidade}: {descricao}, temperatura: {temperatura:.2f}°C")
    
except requests.exceptions.RequestException as e:
    print("Erro ao fazer a solicitação:", e)
except KeyError as e:
    print("Erro ao analisar os dados do clima:", e)




