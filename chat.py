class Chat:
    def __init__(self, pares, reflexoes):
        self.pares = pares
        self.reflexoes = reflexoes

    def respond(self, user_input):
        for chave, valor in self.pares:
            match = chave.match(user_input)

            if match:
                resposta = valor[0]
                return resposta

        return "Desculpe, não entendi o que você disse."

    def converse(self):
        print("Bem-vindo ao Chatbot! (Digite 'sair' para sair)")
        while True:
            try:
                user_input = input("Você: ")
                if user_input.lower() == 'sair':
                    print("Até logo!")
                    break
                else:
                    response = self.respond(user_input)
                    print("Bot:", response)
            except Exception as e:
                print("Ocorreu um erro:", e)
