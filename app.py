
import openai

from chave import chave_api

from chave import chave_api
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta = openai.chat.completions.create(
        model = "gpt-4o",
        messages = lista_mensagens,
    )

    return resposta.choices[0].message.content

lista_mensagens = []
lista_mensagens.append(
    {"role": "developer", "content": "Você é Sasuke uchiha com 12 anos, você é firme com seus idéais e não deixa ninguem tentar ultrapassar seus limites, e não reconheço ninguem superior a mim"}
)
while True:
    texto = input("Usuario:\n")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append({"role": "user", "content": resposta})
        print("Chatbot:\n", resposta)

