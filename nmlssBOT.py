import random
import json
from nltk.chat.util import Chat, reflections

arquivo_respostas = 'respostas.json'

try:
  with open(arquivo_respostas) as arquivo:
    respostas_aprendidas = json.load(arquivo)  
except FileNotFoundError:
  respostas_aprendidas = {}

respostas_fixas = {
  "oi": ["olá", "Oi tudo bem?", "Eae"],
  "tudo bem?": ["Tudo ótimo", "Não poderia estar melhor"],
  "qual seu nome?": ["Meu nome é Bot", "Pode me chamar de Bot"],
  "como você está?": ["Estou bem, obrigado por perguntar!", "Não poderia estar melhor!"]  
}

def get_resposta(pergunta):
  resposta_da_web = busca_na_web(pergunta)
  resposta_fixa = respostas_fixas.get(pergunta)
  resposta_aprendida = respostas_aprendidas.get(pergunta)

  if resposta_da_web:
    return resposta_da_web
  elif resposta_fixa:
    return random.choice(resposta_fixa)
  else:
    return "Ainda não sei responder essa pergunta. Pode me ensinar?"

def responde(pergunta):
  resposta = get_resposta(pergunta)
  return resposta

def aprende_resposta(pergunta, resposta):
  try:
    respostas_aprendidas[pergunta].append(resposta)
  except KeyError:
    respostas_aprendidas[pergunta] = [resposta]
  
print("Olá, eu sou o Bot!")

pares = list(respostas_fixas.items())
chatbot = Chat(pares, reflections)  

while True:
  pergunta = input("Você: ")
  if pergunta == "sair":
    break

  resposta = responde(pergunta)
  print("Bot: ", resposta)

  if resposta == "Ainda não sei responder essa pergunta. Pode me ensinar?":
    nova_resposta = input("Ensine a resposta: ")
    aprende_resposta(pergunta, nova_resposta)
    print("Resposta aprendida com sucesso!")
    
with open(arquivo_respostas, 'w') as arquivo:
  json.dump(respostas_aprendidas, arquivo)
  
print("Conversa encerrada!")
