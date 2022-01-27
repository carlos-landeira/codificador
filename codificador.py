import funcoes

while True:
    codecod = input("Você deseja codificar ou decodificar uma mensagem? ('1' para codificar / '2' para decodificar): ")
    if codecod == "1":
        mensagem = (input("Digite a mensagem para ser codificada:"))
        funcoes.cod_mensagem(mensagem)

    elif codecod == "2":
        funcoes.decod_mensagem()
    elif codecod != "1" and codecod != "2":
        break