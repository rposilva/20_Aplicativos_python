from despesas import Despesas
import json
import os

def carregar_despesas():
    if os.path.exists("despesas.py"):
        with open("despesas.json", "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_despesas(despesas):
    with open("despesas.json", "w") as arquivo:
        json.dump(despesas, arquivo, indent=4, ensure_ascii=False)

def exibir_menu():
    print("\n=== Menu de Despesas ===")
    print("1. Adicionar despesa")
    print("2. Listar despesas")
    print("3. Calcular total de despesas")
    print("4. Calcular despesas por categoria")
    print("5. Calcular despesas recorrentes")
    print("6. Previsão de gastos")
    print("0. Sair")

def main():
    sistema = Despesas()
    sistema.despesas = carregar_despesas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ").strip()
            if not descricao:
                print("❌ A descrição não pode estar vazia!")
                continue
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("❌ Valor inválido! Digite um número.")
                continue
            categoria = input("Categoria: ")
            recorrente_input = input("É recorrente? (s/n): ").strip().lower()
            if recorrente_input not in ["s", "n"]:
                print("❌ Resposta inválida! Use 's' para sim ou 'n' para não.")
                continue
            recorrente = recorrente_input == "s"

            sistema.adicionar_despesa(descricao, valor, categoria, recorrente)
            salvar_despesas(sistema.despesas)
            print(f'Despesa "{descricao}" adicionada com sucesso!')

        elif opcao == "2":
            sistema.listar_despesas()

        elif opcao == "3":
            try:
                sistema.calcular_total_despesas()
            except Exception as e:
                print(f"❌ Erro ao calcular total de despesas: {str(e)}")

        elif opcao == "4":
            sistema.calcular_despesas_por_categoria()

        elif opcao == "5":
            sistema.calcular_despesas_recorrentes()

        elif opcao == "6":
            try:
                meses = int(input("Para quantos meses? "))
                if meses <= 0:
                    print("❌ O número de meses deve ser positivo!")
                    continue
                sistema.previsao_gastos(meses)
            except ValueError:
                print("❌ Por favor, digite um número válido!")
                continue

        elif opcao == "0":
            salvar_despesas(sistema.despesas)
            print("Saindo... Despesas salvas.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# Menu: Receitas
#   1. Adicionar Receita
#   2. Listar Receitas
#   3. Editar Receita
#   4. Remover Receita
#   5. Calcular Receitas Totais
#   6. Previsão de Receitas
#   7. Análise de Economia
#   8. Sair

# Menu: Relatórios
#   1. Relatório de Despesas
#   2. Relatório de Receitas
#   3. Relatório de Economia
#   4. Relatório de Previsão de Gastos
#   5. Sair

# Menu: Configurações
#   1. Configurações Gerais
#   2. Configurações de Notificações
#   3. Configurações de Segurança
#   4. Configurações de Idioma
#   5. Sair

# Menu: Ajuda
#   1. Ajuda Geral
#   2. Ajuda de Despesas
#   3. Ajuda de Receitas
#   4. Ajuda de Relatórios
#   5. Ajuda de Configurações
#   6. Sair

# Menu: Sobre
#   1. Sobre o Aplicativo
#   2. Sobre o Desenvolvedor
#   3. Licença
#   4. Sair