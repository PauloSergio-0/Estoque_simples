from cadastro_fornecedores import *

class ContaPagar:
    def __init__(self, numero_fatura, data_emissao, data_vencimento, valor, descricao, fornecedor_codigo):
        # Inicializa os atributos
        self.numero_fatura = numero_fatura
        self.data_emissao = data_emissao
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.descricao = descricao
        self.fornecedor_codigo = fornecedor_codigo
        self.status_pagamento = "pendente" #a conta já  inicia o status em pedente

class CadastroContasPagar:
    def __init__(self):
        self.contas_pagar = []#inicializa a lista

    def cadastrar_conta_pagar(self, numero_fatura, data_emissao, data_vencimento, valor, descricao, fornecedor_codigo):
        # Cria uma nova instância de ContaPagar com os dados fornecidos
        conta_pagar = ContaPagar(numero_fatura, data_emissao, data_vencimento, valor, descricao, fornecedor_codigo)
        #adiciona a nova conta a lista
        self.contas_pagar.append(conta_pagar)
        print("Conta a pagar cadastrada com sucesso!")

    def atualizar_status_pagamento(self, numero_fatura):
        for conta in self.contas_pagar:
            if conta.numero_fatura == numero_fatura:
                conta.status_pagamento = "pago"# Atualiza o status para "pago"
                print(f"Status de pagamento para a fatura {numero_fatura} atualizado para 'pago'.")
                return True# Retorna True se a atualização foi bem-sucedida
            
        print(f"Fatura {numero_fatura} não encontrada.")
        return False# Retorna True se a atualização foi mal-sucedida
    
    def listar_contas_pagar(self, cadastro_fornecedores):
        #exibi as informações das contas a pagar
        print("\n*** Lista de Contas a Pagar ***\n")
        if not self.contas_pagar:
            print("Nenhuma conta a pagar cadastrada.")
        else:
            for conta in self.contas_pagar:
                print(f"Número da Fatura: {conta.numero_fatura}")
                print(f"Data de Emissão: {conta.data_emissao}")
                print(f"Data de Vencimento: {conta.data_vencimento}")
                print(f"Valor: {conta.valor}")
                print(f"Descrição: {conta.descricao}")
                print(f"Código do Fornecedor: {conta.fornecedor_codigo}")  # Exibe o código do fornecedor
                print(f"Status de Pagamento: {conta.status_pagamento}")
                print("-" * 30)

def menu_cadastro_contas_pagar(cadastro_contas_pagar, cadastro_fornecedores):
    while True:
        numero_fatura = input("Número da fatura: ")
        data_emissao = input("Data de emissão: ")
        data_vencimento = input("Data de vencimento: ")
        valor = float(input("Valor da fatura: "))
        descricao = input("Descrição da fatura: ")

        cadastro_fornecedores.listar_fornecedores_codigo()#lista os fornecedores disponíveis

        fornecedor_codigo = input("Selecione o fornecedor pelo código: ")
        
        if fornecedor_codigo:
            # Chama a função de cadastro de conta a pagar com os dados fornecidos
            cadastro_contas_pagar.cadastrar_conta_pagar(numero_fatura, data_emissao, data_vencimento, valor, descricao, fornecedor_codigo)
            print("Conta a pagar cadastrada com sucesso!")
            break # sai do loop
        else:
            print("Fornecedor não encontrado. Tente novamente.")
