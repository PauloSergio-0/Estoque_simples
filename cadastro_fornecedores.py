class Fornecedor:
    def __init__(self, nome, endereco, telefone, contato, codigo):
        # Inicializa os atributos
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.contato = contato
        self.codigo = codigo


class CadastroFornecedores:
    def __init__(self):
        #inicia a lista fornecedor e o codigo inicial
        self.fornecedores = []
        self.codigo_inicial = 1000
    
    def cadastrar_fornecedor(self, nome, endereco, telefone, contato):
        # verifica se todos os campos foram preenchidos 
        if nome and endereco and telefone and contato:
            #icrementa o codigo inicial e cria um fornecedor
            self.codigo_inicial += 1
            fornecedor = Fornecedor(nome, endereco, telefone, contato, self.codigo_inicial)
            #adiciona o fornecedor a lista
            self.fornecedores.append(fornecedor)
            print("Fornecedor cadastrado com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")

    def listar_fornecedores_codigo(self):
        #lista fornecedores apenas mostrando o nome e  o código
        print("\n*** Lista de Fornecedores ***\n")
        for fornecedor in self.fornecedores:
            print(f"Código do fornecedor: {fornecedor.codigo} | nome: {fornecedor.nome}")

    def obter_fornecedor_por_codigo(self, codigo):
        # Obtém um fornecedor específico com base no código
        for fornecedor in self.fornecedores:
            if str(fornecedor.codigo) == codigo:
                return fornecedor
        return None


    def listar_fornecedores(self):
        #lista todos os dados do fornecedores fornecidos pelo usuario
        print("\n### Lista de Fornecedores ###\n")
        for fornecedor in self.fornecedores:
            print(f"Nome: {fornecedor.nome}\nEndereço: {fornecedor.endereco}\nTelefone: {fornecedor.telefone}\nContato: {fornecedor.contato}\nCódigo do fornecedor: {fornecedor.codigo}")
            print("-" * 30)


def menu_cadastro_fornecedores(cadastro):
    #solicita as informações do usuário
    nome = input("Nome do fornecedor: ")
    endereco = input("Endereço: ")
    telefone = input("Número de telefone: ")
    contato = input("Informações de contato: ")
    cadastro.cadastrar_fornecedor(nome, endereco, telefone, contato)



if __name__ == "__main__":
    # Cria um objeto CadastroFornecedores, executa o menu de cadastro e lista os fornecedores
    cadastro = CadastroFornecedores()
    menu_cadastro_fornecedores(cadastro)
    cadastro.listar_fornecedores()