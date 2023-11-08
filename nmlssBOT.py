import os
import pathlib
import json
import requests
from bs4 import BeautifulSoup
from chat import Chat

arquivo_respostas = pathlib.Path('respostas.json')

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

def busca_na_web(pergunta):
    # (código da função busca_na_web)
    pass

def get_resposta(pergunta):
    resposta_da_web = busca_na_web(pergunta)
    resposta_fixa = respostas_fixas.get(pergunta)
    resposta_aprendida = respostas_aprendidas.get(pergunta)

    if resposta_da_web:
        return resposta_da_web
    elif resposta_fixa:
        return random.choice(resposta_fixa)
    else:
        return "Desculpe, não sei responder essa pergunta."

def responde(pergunta):
    while True:
        pergunta = input("Você: ")
        resposta = get_resposta(pergunta)
        print("Bot:", resposta)

# Executa o chatbot
responde("Teste")
