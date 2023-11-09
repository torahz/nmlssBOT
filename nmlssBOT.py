from colorama import Fore, Style

print(Fore.GREEN + Style.BRIGHT + """
███    ███  █████  ██ ███    ██ 
████  ████ ██   ██ ██ ████   ██ 
██ ████ ██ ███████ ██ ██ ██  ██  
██  ██  ██ ██   ██ ██ ██  ██ ██  
██      ██ ██   ██ ██ ██   ████ 
""" + Style.RESET_ALL)

print("NamelessBOT: Olá! Sobre o que você gostaria de saber?")

while True:

  pergunta = input("Você: ")

  # código para buscar resposta omitido

  print("NamelessBOT:", resposta)

  again = input("NamelessBOT: Você gostaria de saber de algo mais? ")
  if again.lower() == "não" or again.lower() == "n":
    print("NamelessBOT: Tudo bem, tenha um ótimo dia!")
    break

print(Fore.GREEN + "Encerrando o NamelessBOT..." + Style.RESET_ALL)
