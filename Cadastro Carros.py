# Cadastro de Carros pode Modelo, Cor, Ano e Marca
#O programa também deixa você alterar algum dado já diigtado
#Ele também não deixa digitar um ano que não seja um número

class Carros():
    def __init__(self, Modelo, Cor, Ano, Marca):
        self.Modelo = Modelo
        self.Cor = Cor
        self.Ano = Ano
        self.Marca = Marca
    def mudaModelo(self, Modelo): #Função para mudar os atributos 
        self.Modelo = Modelo
    def mudaCor(self, Cor):
        self.Cor = Cor
    def mudaAno(self, Ano):
        self.Ano = Ano
    def mudaMarca(self, Marca):
        self.Marca = Marca       


# Variaveis para coletar os dados
cadastroModelo = (input("Digite o modelo do carro: "))
cadastroCor = str(input("Digite a cor do carro: "))
cadastroMarca = str (input("Digite a marca do carro: "))
cadastroAno = None
while cadastroAno == None:
    try:
        cadastroAno=int(input("Digite o ano do carro: "))
    except ValueError:
            print("O ano precisa ser digitado em números! Por favor tente novamente!")

#Cria um objeto de cadastro, e diz que ela é do tipo Carros, e engloba o que foi atribuido a um carro
CadastroCarros = Carros(cadastroModelo, cadastroCor, cadastroAno, cadastroMarca)

print(f"As informações cadastradas sobre o veículo foram: \n Ano: {cadastroAno}\n Marca: {cadastroMarca}\n Cor: {cadastroCor}\n Modelo: {cadastroModelo}\n")
print(f"Gostaria de alterar alguma informação?\n 1 para SIM\n 2 para NÃO ")
resposta = (input("\nDigite sua opção:\n"))

if resposta == "1":
    print("\nQual opção gostaria de alterar? \n Digite 1 para alterar o ano \n Digite 2 para alterar o modelo \n Digite 3 para alterar a cor \n Digite 4 para alterar a marca  ")
    alteracao = (input("\nDigite sua escolha: "))
    if alteracao == "1":
        print(f"\n O ano cadastrado antes foi {cadastroAno}.")
        alteracaoAno=input("Digite aqui sua nova opção: ")
        CadastroCarros.mudaAno(alteracaoAno)
        print(cadastroAno)
        print(f"\nCadastro de ano alterado para {alteracaoAno} com sucesso!")
    if alteracao == "2":
        print(f"\n O modelo cadastrado antes foi {cadastroModelo}.")
        alteracaoModelo=input("Digite aqui sua nova opção: ")
        CadastroCarros.mudaModelo(alteracaoModelo)
        print(f"\nCadastro de modelo alterado para {alteracaoModelo} com sucesso!")
    if alteracao == "3":
        print(f"\n A cor cadastrada antes foi {cadastroCor}.")
        alteracaoCor=input("Digite aqui sua nova opção: ")
        CadastroCarros.mudaCor(alteracaoCor)
        print(f"\nCadastro de cor alterado para {alteracaoCor} com sucesso!")
    if alteracao == "4":
        print(f"\n A marca cadastrada antes foi {cadastroMarca}.")
        alteracaoMarca=input("Digite aqui sua nova opção: ")
        CadastroCarros.mudaMarca(alteracaoMarca)
        print(f"\nCadastro de marca alterado para {alteracaoMarca} com sucesso!")
else:
    print("Cadastro finalizado com sucesso!")
