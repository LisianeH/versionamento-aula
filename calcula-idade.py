from datetime import datetime

data_nasc = input("Digite sua data de nascimento (dd/mm/yyyy): ")
nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
hoje = datetime.today()
idade = hoje.year - nascimento.year

print(f"Você tem {idade} anos.")

if idade >= 18:
    print("Já pode tirar sua CNH")