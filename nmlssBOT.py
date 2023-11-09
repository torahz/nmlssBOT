import subprocess
import sys 

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Instalando pacote {package}...")
        install(package)

import_or_install('pip') 

import_or_install('requests')
import_or_install('urllib3')

import requests
import urllib.parse

print("NamelessBOT: Olá! O que você precisa saber?")

while True:

  question = input("Você: ")

  url = f"https://api.duckduckgo.com/?q={urllib.parse.quote_plus(question)}&format=json"

  response = requests.get(url)
  data = response.json()

  # Extrai o campo correto com a resposta
  abstract = data["AbstractText"]

  print("NamelessBOT:", abstract)

  again = input("NamelessBOT: Você gostaria de saber de algo mais? ")
  if again.lower() == "não" or again.lower() == "n":
    print("NamelessBOT: Tudo bem, tenha um ótimo dia!")
    break

print("Encerrando o NamelessBOT...")
