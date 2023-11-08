from nltk.chat.util import Chat, reflections

# Adicione pares de perguntas e respostas
pares = [
    ['Eu gosto de (.*)', ['Por que você gosta de \\1?', 'Isso é interessante.']],
    ['Eu sou (.*)', ['Você é \\1?', 'Por que você se identifica como \\1?']],
]

# Adicione reflexões
reflexoes = {
    r'eu sou (.*)': ['Você é \\1?', 'Por que você acha que é \\1?']
}

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
