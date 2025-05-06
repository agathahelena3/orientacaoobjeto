class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.dormindo=False
        self.falando=False

    def falar(self):
        print(f"{self.nome} começou a falar.")
    def comer(self, comida):
        if self.comendo==True:
            print("Não pode comer, pois já está comendo.")
            elif: self.falando==True:
            print("Não pode comer, pois está falando."))

        print(f"{self.nome} foi comer {comida}.")
    def dormir(self):
        print(f"{self.nome} foi dormir.")