import requests
from bs4 import BeautifulSoup
import datetime
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
    descricao, temperatura, umidade, vento = obter_clima(cidade)

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

# Variavéis Tkinter para exibir as informações
clima_info = tk.StringVar()
data_hora = tk.StringVar()

# Rótulo para exibição de data e hora
data_hora_label = ttk.Label(root, textvariable=data_hora)
data_hora_label.pack(pady=10)

# Rótulo para exibição das informações do clima
clima_info_label = ttk.Label(root, textvariable=clima_info, justify="left")
clima_info_label.pack(pady=10)

# Campo de texto para inserir nova locaçização
cidade_entry = ttk.Entry(root, width=30)
cidade_entry.pack(pady=10)

# Botão para buscar informações do clima
buscar_button = ttk.Button(root, text="Buscar Clima", command=atualizar_clima)
buscar_button.pack(pady=10)

# Atualiza a data e hora ao iniciar o aplicativo
atualizar_data_hora()

# Iniciar o loop principal do Tkinter
root.mainloop()