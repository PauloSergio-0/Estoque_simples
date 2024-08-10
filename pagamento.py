from cadastro_contas import *

class Pagamento:
    def __init__(self, conta_pagar, metodo_pagamento, numero_transacao, data_pagamento, comentarios, num_fatura, num_metodo):
        # Inicializa os atributos
        self.conta_pagar = conta_pagar
        self.num_fatura = num_fatura
        self.metodo_pagamento = metodo_pagamento
        self.numero_transacao = numero_transacao
        self.data_pagamento = data_pagamento
        self.num_metodo = num_metodo
        self.comentarios = comentarios

fatura = []  

class CadastroPagamentos:
    def __init__(self, contas_pagar):
        self.pagamentos = []
        self.contas_pagar = contas_pagar

    def realizar_pagamento(self, numero_fatura, metodo_pagamento, num_metodo, numero_transacao, data_pagamento, comentarios):
        # Busca a conta a pagar com o número de fatura fornecido
        conta_pagar = next((c for c in self.contas_pagar.contas_pagar if c.numero_fatura == numero_fatura), None)

        if conta_pagar:
            # Cria uma instância de Pagamento com os dados fornecidos
            pagamento = Pagamento(conta_pagar, metodo_pagamento, numero_transacao, data_pagamento, comentarios, numero_fatura, num_metodo)
            # Atualiza o status de pagamento da conta para "pago"
            conta_pagar.status_pagamento = "pago"
            # Adiciona o pagamento à lista
            self.pagamentos.append(pagamento)
            print("Pagamento efetuado com sucesso!")
            # Atualiza o status de pagamento no cadastro de contas a pagar
            self.contas_pagar.atualizar_status_pagamento(numero_fatura)
        else:
            print("Fatura não encontrada.")

    def listar_pagamentos(self):
        #lista os dados fornecidos se ouver um a conta a pagar
        if not self.pagamentos:
            print("Nenhum pagamento registrado.")
        else:
            print("\n### Lista de Pagamentos ###\n")
            for pagamento in self.pagamentos:
                print(f"Número da Fatura: {pagamento.num_fatura}")
                print(f"Método de Pagamento: {pagamento.metodo_pagamento}")
                print(f"Número do cartão ou cheque: {pagamento.num_metodo}")
                print(f"Número de Transação: {pagamento.numero_transacao}")
                print(f"Data de Pagamento: {pagamento.data_pagamento}")
                print(f"Comentários: {pagamento.comentarios}")
                print("-" * 30)

def menu_cadastro_pagamentos(cadastro_pagamentos):
    #aqui o usuario fornecerá os dados do pagamento
    numero_fatura = input("Número da fatura a pagar: ")
    metodo_pagamento = input("Método de pagamento (cartão ou cheque): ").upper()#deixa tudo em maiúsculo 
    #fornecerá o número para o metodo escolhido
    if metodo_pagamento == "CHEQUE":
        num_metodo = input("Qual o número do Cheque: ")
    elif metodo_pagamento == "CARTÃO" or metodo_pagamento == "CARTAO":
        num_metodo = input("Qual o número do cartão: ")

    numero_transacao = input("Número de transação: ")
    data_pagamento = input("Data de pagamento: ")
    comentarios = input("Notas ou comentários relacionados ao pagamento: ")
    # Chama a função com os dados fornecidos
    cadastro_pagamentos.realizar_pagamento(numero_fatura, metodo_pagamento, num_metodo, numero_transacao, data_pagamento, comentarios)

