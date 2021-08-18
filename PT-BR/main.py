import sqlite3, time, os
from tqdm import tqdm

# Principal class
class Manager:
    # initial function
    def  __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def add(self):
        pass

    def update(self):
        pass    

    def remove(self):
        pass    

    def get_list(self):
        pass

    def terminate(self):
        pass

    def menu(self):
        os.system("cls")
        print("-----------MENU-----------")
        
        time.sleep(0.05)
        print(f"\n1 :) Adicionar")

        time.sleep(0.05)
        print(f"2 :) Remover")

        time.sleep(0.05)
        print(f"3 :) Atualizar")
        
        time.sleep(0.05)
        print(f"4 :) Listar")

        time.sleep(0.05)
        print(f"5 :) Terminar\n")

        opcao = int(input("SELECIONE UMA OPÇÃO :"))
        if opcao == 1:
            self.add()
        elif opcao == 2:
            self.remove()
        elif opcao == 3:
            self.update()
        elif opcao == 4:
            self.get_list()
        elif opcao == 5:
            self.terminate()

        else:
            print("ERROR, TENTE NOVAMENTE AS OPÇÕES 1-5")

            time.sleep(2)
            os.system("cls")
            self.menu()

    def main(self):
        os.system("cls")
        if os.path.isfile("conexao"):
            db = sqlite3.connect("conexao")
            time.sleep(3)
            print()
            print("CONECTADO AO BANCO DE DADOS")
            time.sleep(3)
            self.menu()

        else:
            print("ESTA CONEXÃO NÃO EXISTE\n")
            time.sleep(3)

            print("CRIANDO UMA NOVA CONEXA")
            time.sleep(3)
            

            def loading():
                for _ in tqdm(range(100), desc="carregando...", ascii=False, ncols=75):
                    time.sleep(1)
                print("Carregamento completo!")
                time.sleep(0.50)
            if __name__ == "__main__":
                loading()

            db = sqlite3.connect("conexao")

            cursor = db.cursor()
            cursor.execute("\nCREATE TABLE contacts(Name TEXT, Phone TEXT, Address TEXT)")

            print()

            print("CONEXÃO CRIADA COM SUCESSO")
            print("CONECTADO COM SUCESSO")
            time.sleep(3)
            self.menu()
            
        self.menu()

contacts_manager = Manager()
contacts_manager.main()
