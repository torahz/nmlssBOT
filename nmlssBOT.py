import nltk
from nltk.chat.util import Chat, reflections

# Adicione pares de perguntas e respostas para treinar o chatbot
pares = [
    ['Olá', ['Olá!', 'Oi! Como posso ajudar?']],
    ['Qual é o seu nome?', ['Eu sou um chatbot treinável.', 'Meu nome é ChatGPT.']],
    # Adicione mais pares aqui
]

# Adicione mais reflexões para melhorar as respostas
reflexoes = reflections

# Crie um objeto Chat
chatbot = Chat(pares, reflexoes)

# Função para iniciar a conversa
def converse():
    print("Bem-vindo ao Chatbot! (Digite 'sair' para sair)")
    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() == 'sair':
                print("Até logo!")
                break
            else:
                response = chatbot.respond(user_input)
                print("Bot:", response)
        except Exception as e:
            print("Ocorreu um erro:", e)

# Inicie a conversa
converse()
