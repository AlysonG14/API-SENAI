class Empresa:
    def __init__(self):
        self.historico = []
       


class RH (Empresa):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
       
      
      
        
           
    def operacoes (self):
        while True:
            print("1 - Cadastrar funcionário")
            print("2 - consulta informações do funcionário")
            print("3 - alterar informações do funcionário")
            print("4 - remover informações do funcionário")

            self.operacao = int(input("Digite a operação que você deseja: "))
            print(f"nome: {self.nome}, vocêe escolheeu a opção {self.operacao} ")

            match self.operacao:
                case 1:
                    cadastar = input("Digite o nome do funcionario para cadastrar: ") 
                    self.historico.append(cadastar)
                    print("Usuario cadastrado")
                    return cadastar
                
                case 2:
                    consulta = input("Digite o nome do funcionário que você deseja consultar: ")
                    for funcionario in self.historico:
                        if funcionario == consulta:
                            print(f"funcionario que você esta procurando é {funcionario}")
                        else:
                            funcionario != consulta
                            print('Funcionário não encontrado')
                           
                    return self.historico
                
                case 3:
                    alteracao = input("Digite o nome do funcionario que você deseja alterar as informações: ")
                    self.historico.append(alteracao)
                    return alteracao
                
                case 4:
                    remocao = input("Digite o nome do funcionário que você deseja remover as informações:")
                    for funcionario in self.historico:
                        if remocao == funcionario:
                            self.historico.remove(funcionario)
                    self.historico.append(remocao)
                    return remocao
    def exibindoDados(self):
        return f"a operação é {self.operacao} e as lista de operações é {self.historico}"
    
    def exibindoOperações(self):
        return f''
    

empresa = Empresa()

rh = RH('Vitor')


rh.operacoes()

rh.exibindoDados()

rh.exibindoOperações()
    


    
    


            



