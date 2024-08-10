from cadastro_fornecedores import * # importa as funções necessárias
from cadastro_contas import *
from pagamento import *

def main():#define a função principal
    
    #inicializa os objetos
    cadastro_fornecedores = CadastroFornecedores()
    cadastro_contas_pagar = CadastroContasPagar()
    cadastro_pagamentos = CadastroPagamentos(cadastro_contas_pagar)

    while True:#loop principal
        #menu
        print("\n### Menu Principal ###")
        print("1. Cadastrar Fornecedores")
        print("2. Listar Fornecedores")
        print("3. Cadastrar contas a pagar")
        print("4. Listar contas")
        print("5. Cadastrar Pagamento")
        print("6. Listar Pagamentos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ") #entrada fornecida pelo usuario
        # verifica a entrada
        if opcao == "1":
            menu_cadastro_fornecedores(cadastro_fornecedores)
        elif opcao == "2":
            cadastro_fornecedores.listar_fornecedores()
        elif opcao == "3":
            menu_cadastro_contas_pagar(cadastro_contas_pagar, cadastro_fornecedores)
        elif opcao == "4":
            cadastro_contas_pagar.listar_contas_pagar(cadastro_fornecedores)
        elif opcao == "5":
            menu_cadastro_pagamentos(cadastro_pagamentos)
        elif opcao == "6":
            cadastro_pagamentos.listar_pagamentos()
        elif opcao == "7":# o loop para
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
