#Programa para calcular o valor lógico de:
#P or Q and R 

P = input("Digite o valor de P (true/false): ").strip().lower() == "true"
Q = input("Digite o valor de Q (true/false): ").strip().lower() == "true"
R = input("Digite o valor de R (true/false): ").strip().lower() == "true"

if  P or (Q and R):
    print("True")
else:
    print("False")