import random
import nltk
from nltk.chat.util import Chat, reflections

# Respostas iniciais 
respostas = {
  "oi": ["olá", "Oi tudo bem?", "Eae"],
  "tudo bem?": ["Tudo ótimo", "Não poderia estar melhor"],
  "qual seu nome?": ["Meu nome é Bot", "Pode me chamar de Bot"],
  "como você está?": ["Estou bem, obrigado por perguntar!","Não poderia estar melhor!"]
}

# Respostas aprendidas
respostas_aprendidas = {} 

def responde(pergunta):
  if pergunta in respostas:
    return random.choice(respostas[pergunta])
  elif pergunta in respostas_aprendidas:
    return random.choice(respostas_aprendidas[pergunta])
  else:
    return "Ainda não sei responder essa pergunta. Pode me ensinar?"

def aprende_resposta(pergunta, resposta):
  if pergunta not in respostas_aprendidas:
    respostas_aprendidas[pergunta] = []
  respostas_aprendidas[pergunta].append(resposta)

print("Olá, eu sou o Bot!")

chatbot = Chat(respostas, reflections)

while True:
  pergunta = input("Você: ")
  if pergunta == "sair":
    print("Bot: Tchau!")  
    break

  resposta = responde(pergunta)
  print("Bot: ", resposta)

  if resposta == "Ainda não sei responder essa pergunta. Pode me ensinar?":
    resposta_ensinada = input("Ensine a resposta: ")
    aprende_resposta(pergunta, resposta_ensinada)
    print("Resposta aprendida com sucesso!")

print("Conversa encerrada")
