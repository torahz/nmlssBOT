import nltk
import wikipedia

print("NamelessBOT: Olá! O que você precisa saber?")

while True:
  question = input("Você: ")

  # Busca a resposta na Wikipedia
  try:
    response = wikipedia.summary(question, sentences=2)
  except wikipedia.exceptions.PageError:
    response = "Desculpe, não encontrei uma resposta para essa pergunta."

  print("NamelessBOT:", response)

  again = input("NamelessBOT: Você gostaria de saber de algo mais? ")
  if again.lower() == "não" or again.lower() == "n":
    print("NamelessBOT: Tudo bem, tenha um ótimo dia!")
    break

print("Encerrando o NamelessBOT...")
