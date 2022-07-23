import mysql.connector

class Cadastra_veiculo:
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, km: float, motor: str):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.km = km
        self.motor = motor
        self.id = 0  # No Banco de Dados esse campo será preenchido automaticamente

    def conexao_banco(self):
        # Criando a conexão
        myconnection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='654321',
            database='concessionaria',
        )

        cursor = myconnection.cursor()

        # Comando SQL para inserir valores dentro da tabela veiculos
        comando = f'INSERT INTO veiculos VALUES ("{self.id}", "{self.placa}","{self.modelo}","{self.marca}",' \
                  f'"{self.ano}", "{self.cor}", "{self.km}", "{self.motor}")'

        cursor.execute(comando)
        myconnection.commit()

        cursor.close()
        myconnection.close()  # encerrando a conexão
