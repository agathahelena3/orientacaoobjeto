class Conta():
    def __init__(self, nome, numero_da_conta, tipo_da_conta):
        self.nome=nome
        self.numero_da_conta=numero_da_conta
        self.tipo_da_conta=tipo_da_conta
        self.status_da_conta= False
        self.saldo= 0

    def ativar (self):
        self.status_da_conta= True

    def depositar (self):
        self.saldo = int(input("Digite o valor que deseja depositar:"))
        print (f"Seu saldo atual é de {self.saldo}")

    def sacar (self):
       sacar = self.saldo = int(input("Digite o valor que deseja sacar:"))
       if sacar > self.saldo:
           print ("Saldo insuficiente.")
       else:
           print ("Saque efetuado.")
           self.saldo = self.saldo = sacar
           print (self.saldo)

