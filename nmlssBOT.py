import requests
from bs4 import BeautifulSoup

print("NamelessBOT: Olá! Sobre o que você gostaria de saber?")

while True:

  pergunta = input("Você: ")

  url = f"https://desciclopedia.org/wiki/{pergunta}"
  resposta = requests.get(url)

  soup = BeautifulSoup(resposta.text, 'html.parser')
  conteudo = soup.find('div', {'class': 'mw-parser-output'})

  if conteudo is None:
    print("NamelessBOT: Desculpe, não encontrei uma resposta para isso na Desciclopédia.")
  else:
    print("NamelessBOT:", conteudo.text)

  again = input("NamelessBOT: Você gostaria de saber de algo mais? ")
  if again.lower() == "não" or again.lower() == "n":
    print("NamelessBOT: Tudo bem, tenha um ótimo dia!")
    break

print("Encerrando o NamelessBOT...")
