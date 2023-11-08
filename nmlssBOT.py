import json
import random
from nltk.chat.util import Chat, reflections

arquivo_respostas = 'respostas.json'

try:
  with open(arquivo_respostas, 'r') as arquivo:
    respostas_aprendidas = json.load(arquivo)
except FileNotFoundError:
  respostas_aprendidas = {}

respostas_fixas = {
  "oi": ["olá", "Oi tudo bem?", "Eae"],
  "tudo bem?": ["Tudo ótimo", "Não poderia estar melhor"],
  "qual seu nome?": ["Meu nome é Bot", "Pode me chamar de Bot"],
  "como você está?": ["Estou bem, obrigado por perguntar!", "Não poderia estar melhor!"]
}

with open('dicptbrverb.txt', 'r') as arquivo:
  dicionario = json.load(arquivo)

def busca_na_web(pergunta):
  
  resposta = "" #busca na web e extrai resposta
  
  return resposta

def busca_no_dicionario(pergunta):

  resposta = "" #busca palavras relacionadas e forma resposta

  return resposta

def responde(pergunta):

  resposta = busca_na_web(pergunta)

  if not resposta:

    resposta = busca_no_dicionario(pergunta)

    if not resposta:
    
      if pergunta in respostas_fixas:
        resposta = random.choice(respostas_fixas[pergunta])
        
      elif pergunta in respostas_aprendidas:
        resposta = random.choice(respostas_aprendidas[pergunta])
        
      else:
        resposta = "Ainda não sei responder essa pergunta. Pode me ensinar?"

  return resposta

# resto do código... 

# salva respostas aprendidas
