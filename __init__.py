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
            host='',  #local ondé esta o banco de dados
            user='',  #nome do usuario
            password='',  #senha
            database='',  #nome do banco de dados
        )

        cursor = myconnection.cursor()

        # Comando SQL para inserir valores dentro da tabela veiculos
        comando = f'INSERT INTO (nome da tabela) VALUES ("{self.id}", "{self.placa}","{self.modelo}","{self.marca}",' \
                  f'"{self.ano}", "{self.cor}", "{self.km}", "{self.motor}")'

        cursor.execute(comando)
        myconnection.commit()

        cursor.close()
        myconnection.close()  # encerrando a conexão
