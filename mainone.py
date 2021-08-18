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
        print(f"\n1 :) Add")

        time.sleep(0.05)
        print(f"2 :) Remove")

        time.sleep(0.05)
        print(f"3 :) Update")
        
        time.sleep(0.05)
        print(f"4 :) List")

        time.sleep(0.05)
        print(f"5 :) Terminate\n")

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
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            print()
            print("CONECTADO AO BANCO DE DADOS")
            time.sleep(3)
            self.menu()

        else:
            print("ESTA CONECÇÃO NÃO EXISTE\n")
            time.sleep(3)

            print("Creating new connection file")
            time.sleep(3)
            

            def loading():
                for _ in tqdm(range(50), desc="Loading...", ascii=False, ncols=75):
                    time.sleep(0.10)
                print("Loading Done!")
                time.sleep(0.50)
            if __name__ == "__main__":
                loading()

            db = sqlite3.connect("connection")

            cursor = db.cursor()
            cursor.execute("\nCREATE TABLE contacts(Name TEXT, Phone TEXT, Address TEXT)")

            print()

            print("CONEÃO CRIADA COM SUCESSO")
            print("CONECTADO COM SUCESSO")
            time.sleep(3)
            self.menu()
            
        self.menu()

contacts_manager = Manager()
contacts_manager.main()
