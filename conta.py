class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo é de {self.__saldo} do titular {self.__titular}")

    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= self.__limite
        else:
            print(f"O valor {valor} ultrapassou o limite")

    def deposita(self, valor):
        self.__saldo += valor

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @staticmethod
    def codigo_banco():
        return "001"


teste = Conta(123, "Lucas", 100.0)
print(teste)

teste.extrato()
