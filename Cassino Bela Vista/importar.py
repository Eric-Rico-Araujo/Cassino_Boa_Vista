def login():

    usuarios = {
        "eric":"1234",
        "debora":"123",
        "debsfraga":"debs123"
    }

    usuario = input("Digite seu nome de usuario:")
    senha = input("Digite sua senha:")

    if usuario and usuarios[usuario] == senha:
        print("Acesso permitido")
    else:
        print("Acesso negado")

login()