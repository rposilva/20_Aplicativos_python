# Menu: Despesas
#   1. Adicionar Despesa
#   2. Listar Despesas
#   3. Editar Despesa
#   4. Remover Despesa
#   5. Calcular Despesas Totais
#   6. Previsão de Gastos
#   7. Análise de Economia
#   8. Sair
from despesas import Despesas

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

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            valor = float(input("Valor: "))
            categoria = input("Categoria: ")
            recorrente = input("É recorrente? (s/n): ").strip().lower() == 's'

            sistema.adicionar_despesa(descricao, valor, categoria, recorrente)
            print(f'Despesa "{descricao}" adicionada com sucesso!')

        elif opcao == "2":
            sistema.listar_despesas()

        elif opcao == "3":
            sistema.calcular_total_despesas()

        elif opcao == "4":
            sistema.calcular_despesas_por_categoria()

        elif opcao == "5":
            sistema.calcular_despesas_recorrentes()

        elif opcao == "6":
            meses = int(input("Para quantos meses? "))
            sistema.previsao_gastos(meses)

        elif opcao == "0":
            print("Saindo...")
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