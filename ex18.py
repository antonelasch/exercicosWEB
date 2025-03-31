val_temp = int(input("Informe a temperatura: "))
selecionada = input("Informe qual é a temperatura que você deseja converter (C/F/K): ")
saida = input("Informe qual é a temperatura que será a saída (C/F/K): ")

if selecionada == 'C':
    if saida == 'F':
        resultado = (val_temp * 9/5) + 32
    elif saida == 'K':
        resultado = val_temp + 273.15
elif selecionada == 'F':
    if saida == 'C':
        resultado = (val_temp - 32) * 5/9
    elif saida == 'K':
        resultado = (val_temp - 32) * 5/9 + 273.15
elif selecionada == 'K':
    if saida == 'C':
        resultado = val_temp - 273.15
    elif saida == 'F':
        resultado = (val_temp - 273.15) * 9/5 + 32

print("Temperatura convertida: ", resultado)

#não consegui terminar essa e nem fazer a 19