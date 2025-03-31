salario = int(input("Informe o salário do funcionário: "))
perc_aumento = int(input("Informe o percentual de aumento: "))

aumento = salario * perc_aumento / 100
val_aumento = salario + aumento

print("O valor do aumento é", aumento)

print("O valor do salário após o aumento é", val_aumento)
