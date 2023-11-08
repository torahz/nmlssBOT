import requests
from bs4 import BeautifulSoup
from chat import Chat

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

def busca_na_web(pergunta):
    """
    Faz uma busca no Google e retorna uma resposta concisa.

    Args:
        pergunta: A pergunta a ser buscada.

    Returns:
        Uma resposta concisa da web, ou None se não for encontrada.
    """

    # Fazer uma solicitação HTTP para o Google

    url = "https://www.google.com/search?q=" + pergunta
    resposta = requests.get(url)

    # Extrair a resposta da solicitação

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, 'html.parser')
        resultado = soup.find("div", class_="g")
        resposta_resumida = resultado.find("span").text
        return resposta_resumida
    else:
        return None

def get_resposta(pergunta):
    resposta_da_web = busca_na_web(pergunta)
    resposta_fixa = respostas_fixas.get(pergunta)
    resposta_aprendida = respostas_aprendidas.get(pergunta)

    if resposta_da_web:
        return resposta_da_web
    elif resposta_fixa:
        return resposta_fixa
    else:
        return "Ainda não sei responder essa pergunta. Pode me ensinar?"

def responde(pergunta):
    pares = list(respostas_fixas.items())
    chatbot = Chat(pares, reflections)

    resposta = get_resposta(pergunta)
    print("Bot: ", resposta)

if arquivo_respostas.is_file():
    with open(arquivo_respostas, 'w') as arquivo:
        json.dump(respostas_aprendidas, arquivo)

print("Conversa encerrada!")
