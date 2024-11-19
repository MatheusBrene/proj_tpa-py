import Pessoa
res = 0
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: "))
    return res

cadastro = []

res = pergunta()
while(res== 1):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salario da pessoa: "))
    
    cadastro.append(Pessoa(nome, idade, cargo, salario))
    pergunta()
    