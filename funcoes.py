alfabeto = {"a": "fpx", "b": "png", "c": "rdp", "d": "red",
            "e": "skt", "f": "kbm", "g": "itz", "h": "fla",
            "i": "rns", "j": "fnc", "k": "dwn", "l": "one",
            "m": "prg", "n": "ssg", "o": "ssw", "p": "fur",
            "q": "san", "r": "flk", "s": "hvn", "t": "g2e",
            "u": "c9e", "v": "grf", "w": "ing", "x": "tml",
            "y": "edg", "z": "cnb", " ": "roy"}


def cod_mensagem(mensagem):

    mensagem_codificada = ""
    for letra in mensagem:
        mensagem_codificada += alfabeto[letra]
    arq = open("mensagem.txt","w")
    arq.write(mensagem_codificada)
    arq = open("mensagem.txt","r")
    mensagem_txt = arq.read()
    print("Mensagem codificada é: {}".format(mensagem_txt))

def decod_mensagem():

    arq = open("mensagem.txt","r")
    decod = arq.read()
    msg_orig = ""
    arq.close()
    for i in range(0, len(decod), 3):
        for chave, valor in alfabeto.items():
            if valor == decod[i:i+3]:
                break
        msg_orig += chave
    print("Mensagem decodificada é: {}".format(msg_orig))