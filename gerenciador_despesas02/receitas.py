class Receitas:
    """Classe para gerenciar uma coleção de receitas."""
    def __init__(self):
        """Inicializa uma nova instância da classe Receitas."""
        self.receitas = []

    def adicionar_receita(self, descricao, valor, categoria):
        receita = {
            'descricao': descricao,
            'valor': valor,
            'categoria': categoria
        }
        self.receitas.append(receita)
        print(f'Receita "{descricao}" adicionada com sucesso!')

    def listar_receitas(self):
        if not self.receitas:
            print("Nenhuma receita cadastrada.")
            return
        print("Lista de receitas:")
        for i, receita in enumerate(self.receitas, start=1):
            print(f"{i}. {receita['descricao']} - R$ {receita['valor']} - Categoria: {receita['categoria']}")

    def calcular_total_receitas(self):
        total = sum(receita['valor'] for receita in self.receitas)
        print(f"Total de receitas: R$ {total:.2f}")
        return total

    def calcular_receitas_por_categoria(self):
        categorias = {}
        for receita in self.receitas:
            categoria = receita['categoria']
            if categoria not in categorias:
                categorias[categoria] = 0
            categorias[categoria] += receita['valor']

        print("Total de receitas por Categoria:")
        for categoria, total in categorias.items():
            print(f"{categoria}: R$ {total:.2f}")

    def calcular_receitas_recorrentes(self):
        recorrentes = []
        for receita in self.receitas:
            if receita.get('recorrente', False):
                recorrentes.append(receita)

        total_recorrentes = sum(receita['valor'] for receita in recorrentes)
        print(f"Total de receitas Recorrentes: R$ {total_recorrentes:.2f}")
        return total_recorrentes

    def previsao_receitas(self, meses=3):
        if not self.receitas:
            print("Nenhuma receita cadastrada.")
            return None

        total_receitas = self.calcular_total_receitas()
        previsao = total_receitas * meses
        print(f"Previsão de Gastos para os próximos {meses} meses: R$ {previsao:.2f}")
        return previsao

