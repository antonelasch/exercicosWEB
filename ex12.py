nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7: print("O aluno foi APROVADO")

elif media >= 5 and media < 7: print("O aluno está em RECUPERAÇÃO'")
        
else: print("ALUNO REPROVADO")
