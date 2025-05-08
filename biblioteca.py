class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.dormindo=False
        self.falando=False

    def falar(self):
        if self.comendo==True:
            print("Não pode falar, pois está comendo.")
        elif self.falando==True:
            print("Já está falando.")
        elif self.dormindo==True:
            print("Não pode falar, pois está dormindo.")
        else:
         print(f"{self.nome} começou a falar.")
         self.falando=True

    def parar_de_falar(self):
        if self.falando == True:
          print(f"{self.nome} parou de falar.")
        else:
          print(f"{self.nome} já está calado.")

    def comer(self, comida):
        if self.comendo==True:
            print("Já está comendo.")
        elif self.falando==True:
            print("Não pode comer, pois está falando.")
        elif self.dormindo==True:
            print("Não pode comer, pois está dormindo.")
        else:
         print(f"{self.nome} foi comer {comida}.")
         self.comendo=True

    def parar_de_comer(self):
        if self.comendo == True:
          print(f"{self.nome} parou de comer.")
        else:
          print(f"{self.nome} já não está comendo.")


    def dormir(self):
        if self.comendo==True:
            print("Não pode dormir, pois está comendo.")
        elif self.falando==True:
            print("Não pode dormir, pois está falando.")
        elif self.dormindo==True:
            print("Já está dormindo.")
        else:
         print(f"{self.nome} foi dormir.")
         self.dormindo = True

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou.")
        else:
            print (f"{self.nome} já está acordado.")
