from colorama import Fore, Style
import requests 
from bs4 import BeautifulSoup

print(Fore.YELLOW + Style.BRIGHT + """
███   ██ ███████ ██    ██ █████ ██   █████ ██████ ██████ █████  ██████ ████████
████  ██ ██   ██ ███  ███ ██    ██   ██    ██     ██     ██   █ ██   █    ██
██ ██ ██ ███████ ██ ██ ██ █████ ██   █████ ██████ ██████ █████  ██   █    ██
██  ████ ██   ██ ██    ██ ██    ██   ██        ██     ██ ██   █ ██   █    ██
██    ██ ██   ██ ██    ██ █████ ████ █████ ██████ ██████ █████  ██████    ██
""" + Style.RESET_ALL)

print("nmlssBOT: Olá! Sobre o que você gostaria de saber?")

while True:

  pergunta = input("Você: ")

  url = f"https://desciclopedia.org/wiki/{pergunta}"
  resposta = requests.get(url)

  soup = BeautifulSoup(resposta.text, 'html.parser')
  conteudo = soup.find('div', {'class': 'mw-parser-output'})

  if conteudo is None:
    resposta = "Desculpe, não encontrei uma resposta para isso na Desciclopédia."
  else:
    resposta = conteudo.text

  print("nmlssBOT:", resposta)

  again = input("nmlssBOT: Você gostaria de saber de algo mais? ")
  if again.lower() == "não" or again.lower() == "n":
    print("nmlssBOT: Tudo bem, tenha um ótimo dia!")
    break

print(Fore.YELLOW + "Encerrando o nmlssBOT..." + Style.RESET_ALL)
