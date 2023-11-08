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

def responde(pergunta):
  if pergunta in respostas_fixas:
    return random.choice(respostas_fixas[pergunta])
  elif pergunta in respostas_aprendidas:
    return random.choice(respostas_aprendidas[pergunta])
  else:
    return "Ainda não sei responder essa pergunta. Pode me ensinar?"

def aprende_resposta(pergunta, resposta):
  if pergunta not in respostas_aprendidas:
    respostas_aprendidas[pergunta] = []
  respostas_aprendidas[pergunta].append(resposta)
  
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
