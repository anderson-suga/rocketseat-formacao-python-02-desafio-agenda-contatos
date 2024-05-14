def ok_input_favorito(favorito):
    if favorito.upper() in ["S", "N"]:
        return True
    return False


def adicionar_contato(contatos, nome, telefone, email, favorito):
    status = True if favorito.upper() == "S" else False
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": status}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado com sucesso.")
    return


def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "✓" if contato["favorito"] else " "
        print(
            f"{indice}. Nome: {nome} - Telefone: {telefone} - E-mail: {email} - [{favorito}] Favorito"
        )
    return


def atualizar_contato(
    contatos, indice_contato, novo_nome, novo_telefone, novo_email, novo_favorito
):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        favorito = True if novo_favorito.upper() == "S" else False
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        contatos[indice_contato_ajustado]["favorito"] = favorito
        print(f"Contato {indice_contato} atualizado para {novo_nome}")
    else:
        print("Índice do contato inválido.")
    return


def marca_desmarca_favorito(contatos, indice_contato, novo_favorito):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        favorito = True if novo_favorito.upper() == "S" else False
        contatos[indice_contato_ajustado]["favorito"] = favorito
        print(f"Contato {indice_contato} atualizado")
    else:
        print("Índice do contato inválido.")
    return


def listar_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. Nome: {nome} - Telefone: {telefone} - E-mail: {email}")
    return


def excluir_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        nome = contato_removido["nome"]
        telefone = contato_removido["telefone"]
        email = contato_removido["email"]
        print(
            f"Contato removido: Nome: {nome} - Telefone: {telefone} - E-mail: {email}"
        )
    else:
        print("Índice do contato inválido.")
    return


contatos = []

while True:
    print("\nMenu do Gerenciador de Lista de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contatos")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Listar favoritos")
    print("6. Apagar contatos")
    print("7. Sair")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o telefone do novo contato: ")
        email = input("Digite o e-mail do novo contato: ")
        favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        while not ok_input_favorito(favorito):
            favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        adicionar_contato(contatos, nome, telefone, email, favorito)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo e-mail do contato: ")
        novo_favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        while not ok_input_favorito(novo_favorito):
            novo_favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        atualizar_contato(
            contatos,
            indice_contato,
            novo_nome,
            novo_telefone,
            novo_email,
            novo_favorito,
        )
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o número do contato que deseja marcar/desmarcar como favorito: "
        )
        novo_favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        while not ok_input_favorito(novo_favorito):
            novo_favorito = input("Contato favorito?\n(S/s) Sim\n(N/n) Não\n")
        marca_desmarca_favorito(contatos, indice_contato, novo_favorito)
    elif escolha == "5":
        listar_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja excluir: ")
        excluir_contato(contatos, indice_contato)
        ver_contatos(contatos)
    elif escolha == "7":
        break

print("Programa finalizado")
