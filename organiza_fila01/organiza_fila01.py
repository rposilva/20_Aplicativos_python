import datetime

# Organizador de Fila de Atendimento
fila = [] # Lista para armazenar os nomes na fila
tempos_espera = [] # Lista para armazenar os tempos de espera
contador_senhas = 1
ultima_senha_atendida = None

def cadastro(nome):
    global contador_senhas
    hora_chegada = datetime.datetime.now()  # Define hora_chegada
    pessoa = {
        "nome": nome,
        "hora_chegada": hora_chegada,
        "senha": contador_senhas
    }  # Cria um dicionário com os dados da pessoa
    fila.append(pessoa)
    print(f"{nome}, você recebeu a senha N° {contador_senhas} às {hora_chegada.strftime('%H:%M:%S')}")
    contador_senhas += 1  # Incrementa o contador de senhas

def atender():
    global ultima_senha_atendida
    if not fila:
        print("Fila vazia.")
        return
    pessoa = fila.pop(0)  # Remove a primeira pessoa da fila
    hora_atendimento = datetime.datetime.now()  # Define hora_atendimento
    espera = hora_atendimento - pessoa["hora_chegada"]  # Calcula o tempo de espera
    tempos_espera.append(espera)  # Adiciona o tempo de espera à lista
    ultima_senha_atendida = pessoa["senha"]  # Atualiza a última senha atendida

    print(f"\n🔔 ATENDENDO: {pessoa['nome']} (Senha Nº {pessoa['senha']})")    
    print(f"Hora de atendimento: {hora_atendimento.strftime('%H:%M:%S')}")
    print(f"Tempo de espera: {espera}")
    
def tempo_medio():
    if not tempos_espera:
        print("Nenhum atendimento ainda.")
        return
    media = sum(tempos_espera, datetime.timedelta()) / len(tempos_espera)  # Calcula o tempo médio de espera
    print(f"⏱ Tempo médio de espera: {media}")
    
def mostrar_painel():
    if ultima_senha_atendida is None:
        print("Nenhum atendimento realizado.")
    else:
        print(f"📺 Última senha atendida: N° {ultima_senha_atendida}")
    
def menu():
    while True:
        print("\n--- Menu ---:")
        print("1 - Adicionar pessoa")
        print("2 - Atender próxima pessoa")
        print("3 - Mostrar tempo médio de espera")
        print("4 - Mostrar painel de senhas")
        print("0 - Sair")        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                nome = input("Digite o nome da pessoa: ")
                cadastro(nome)
            case "2":
                atender()
            case "3":
                tempo_medio()
            case "4":
                mostrar_painel()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

menu()