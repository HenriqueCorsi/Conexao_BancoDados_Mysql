from mysql_connector_ import *

print('    CADASTRO DE VEÍCULOS    ')
try:
    placa = str(input('Placa: '))
    modelo = str(input('Modelo: '))
    marca = str(input('Marca: '))
    ano = int(input('Ano: '))
    cor = str(input('Cor: '))
    km = float(input('KM atual: '))
    motor = str(input('Motor: '))
except (ValueError, TypeError):
    print('Informação inválida')
else:
    # Criando os objetos
    veiculo01 = Cadastra_veiculo(placa, modelo, marca, ano, cor, km, motor)

    # Executando o método responsável por inserir os dados dentor do banco de d ados
    veiculo01.conexao_banco()

    print('Cadastro realizado com sucesso!')
