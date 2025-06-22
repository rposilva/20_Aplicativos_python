class Despesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor, categoria, recorrente=False):
        despesa = {
            'descricao': descricao,
            'valor': valor,
            'categoria': categoria,
            'recorrente': recorrente
        }
        self.despesas.append(despesa)
        print(f'Despesa "{descricao}" adicionada com sucesso!')

    def listar_despesas(self):
        if not self.despesas:
            print("Nenhuma despesa cadastrada.")
            return
        print("Lista de Despesas:")
        for i, despesa in enumerate(self.despesas, start=1):
            print(f"{i}. {despesa['descricao']} - R$ {despesa['valor']} - Categoria: {despesa['categoria']}")

    def calcular_total_despesas(self):
        total = sum(despesa['valor'] for despesa in self.despesas)
        print(f"Total de Despesas: R$ {total:.2f}")
        return total
    
    def calcular_despesas_por_categoria(self):
        categorias = {}
        for despesa in self.despesas:
            categoria = despesa['categoria']
            if categoria not in categorias:
                categorias[categoria] = 0
            categorias[categoria] += despesa['valor']
        
        print("Total de Despesas por Categoria:")
        for categoria, total in categorias.items():
            print(f"{categoria}: R$ {total:.2f}")
            
    def calcular_despesas_recorrentes(self):
        recorrentes = []
        for despesa in self.despesas:
            if despesa.get('recorrente', False):
                recorrentes.append(despesa)
        
        total_recorrentes = sum(despesa['valor'] for despesa in recorrentes)
        print(f"Total de Despesas Recorrentes: R$ {total_recorrentes:.2f}")
        return total_recorrentes
    
    def previsao_gastos(self, meses=3):
        if not self.despesas:
            print("Nenhuma despesa cadastrada.")
            return None
        
        total_despesas = self.calcular_total_despesas()
        previsao = total_despesas * meses
        print(f"Previsão de Gastos para os próximos {meses} meses: R$ {previsao:.2f}")
        return previsao

