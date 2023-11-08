class Chat:
    def __init__(self, pares, reflections):
        self.pares = pares
        self.reflections = reflections

    def respond(self, pergunta):
        resposta = get_resposta(pergunta)
        return resposta
